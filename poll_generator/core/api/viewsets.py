from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from core import models
from core.api import serializers


class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.filter(active=True)
    serializer_class = serializers.PollSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = models.Option.objects.all()
    serializer_class = serializers.OptionSerializer

    @action(detail=True, methods=['get'])
    def vote(self, request, pk=None):
        option = self.get_object()
        option.register_vote()
        return Response({'message': 'voto registrado'})
