import uuid
from django.db import models
from django.db.models.base import Model
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

    def send_status(self):
        """
        Obtém os resultados da enquete atual e os envia via websockets.
        """
        results = {'poll_id': str(self.id), 'options': []}
        for result in self.options.all():
            results['options'].append({result.description : result.votes})

        async_to_sync(get_channel_layer().group_send)(
            "results_poll_room",
            {
                "type": "chat.message",
                "message": results,
            }
        )


class Option(models.Model):
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

    def register_vote(self):
        self.votes += 1
        self.save()
