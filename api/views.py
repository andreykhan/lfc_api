from .models import Players, Coaches
from .serializers import PlayersSerialiazer, CoachesSerializer
from rest_framework import viewsets


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerialiazer


class CoachesViewSet(viewsets.ModelViewSet):
    queryset = Coaches.objects.all()
    serializer_class = CoachesSerializer
