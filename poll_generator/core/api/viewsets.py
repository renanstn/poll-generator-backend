from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from core import models
from core.api import serializers


class PollViewSet(viewsets.ModelViewSet):
    """
    ViewSet para controle das enquetes.
    """

    # A queryset é definica dinamicamente de acordo com o query param 'active'
    serializer_class = serializers.PollSerializer

    def get_queryset(self):
        active_param = self.request.query_params.get('active', False)
        if active_param:
            active = True if active_param == '1' else False
            return models.Poll.objects.filter(active=active)
        else:
            return models.Poll.objects.all()


class OptionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para controle das opções de cada enquete, assim como o
    recebimento de votos em cada uma.
    """

    queryset = models.Option.objects.all()
    serializer_class = serializers.OptionSerializer

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None) -> Response:
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
