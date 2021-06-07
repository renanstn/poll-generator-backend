import uuid
from django.db import models
from django.db.models.constraints import UniqueConstraint


class Poll(models.Model):
    """
    Model que armazena as enquetes criadas.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


class Option(models.Model):
    """
    Model que armazena as opções de cada enquete, assim como a quantidade
    de votos que cada opção recebeu.
    Também implementa um método de controle para checar se um user pode
    ou não votar em uma enquete.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='options'
    )
    description = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.description

    def check_if_user_can_vote(self, session_id: str) -> bool:
        """
        Retorna se um usuário pode votar em uma enquete, verificando se a
        'session_id' do navegador dele já está registrada na tabela de
        VotesControl.
        """
        return not VotesControl.objects.filter(
            session_id=session_id,
            poll=self.poll
        ).exists()

    def register_vote(self, session_id: str):
        """
        Registra o voto do usuário em uma opção, e salva sua 'session_id' na
        model VotesControl para ter controle dos votos.
        """
        self.votes += 1
        self.save()
        VotesControl.objects.create(
            session_id=session_id,
            poll=self.poll
        )


class VotesControl(models.Model):
    """
    Model que faz o controle de "quem votou em quê".
    Ela garante que cada sessão de usuário possa votar somente uma vez em
    cada enquete.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    session_id = models.CharField(max_length=16)
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='sessions'
    )

    def __str__(self) -> str:
        return f"{self.session_id} - {self.poll.title}"

    class Meta:
        constraints = [
            # Essa constraint garante que cada par de 'poll' e 'session_id'
            # sejam únicos.
            models.UniqueConstraint(
                fields=['session_id', 'poll'],
                name="Voto único"
            )
        ]
