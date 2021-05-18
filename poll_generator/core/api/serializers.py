from rest_framework import serializers
from core import models


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Option
        fields = (
            'id',
            'description',
            'votes',
        )


class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = models.Poll
        fields = (
            'id',
            'active',
            'title',
            'options',
        )

    def create(self, validated_data):
        """
        Sempre que precisar salvar no mesmo POST relações de ForeignKey, este
        método deve ser reescrito.
        """
        options = validated_data.pop('options')
        poll = models.Poll.objects.create(**validated_data)
        for option in options:
            models.Option.objects.create(poll=poll, **option)
        return poll
