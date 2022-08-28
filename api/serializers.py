from rest_framework import serializers
from .models import Players, Coaches


class PlayersSerialiazer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Players


class CoachesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Coaches