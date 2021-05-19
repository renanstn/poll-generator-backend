import uuid
from django.db import models
from django.db.models.base import Model


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title


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
