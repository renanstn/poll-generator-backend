from rest_framework import viewsets, status
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

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        option = self.get_object()
        can_vote = option.register_vote(request.data.get('session_id'))
        if can_vote:
            option.poll.send_status()
            return Response({'message': 'Voto registrado'})
        else:
            return Response(
                {'message': 'Você já votou nessa enquete'},
                status=status.HTTP_208_ALREADY_REPORTED
            )
