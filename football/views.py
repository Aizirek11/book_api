from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Coach, Team, Player, Tournament
from .serializers import (
    CoachSerializer,
    TeamSerializer,
    PlayerSerializer,
    TournamentSerializer
)


class CoachViewSet(ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TournamentViewSet(ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer



# Create your views here.
