from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
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
        poll_serializer = serializers.PollSerializer(option.poll)
        can_vote = option.check_if_user_can_vote(request.data.get('session_id'))
        # can_vote = True
        if can_vote:
            # Registra o voto
            option.register_vote(request.data.get('session_id'))
            # Envia signal websocket para atualizar
            async_to_sync(get_channel_layer().group_send)(
                "results_poll_room",
                {
                    "type": "chat.message",
                    "message": poll_serializer.data,
                }
            )

            return Response(
                {'message': 'Voto registrado'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': 'Você já votou nessa enquete'},
                status=status.HTTP_208_ALREADY_REPORTED
            )
