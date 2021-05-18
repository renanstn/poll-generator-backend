from rest_framework import viewsets
from core import models
from core.api import serializers
from core.websocket import consumers


class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.filter(active=True)
    serializer_class = serializers.PollSerializer

    def create(self, request, *args, **kwargs):
        # consumer = consumers.Consumer()
        # consumer.send(text_data='olaaaaaaaaa')
        return super().create(request, *args, **kwargs)
