from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoachViewSet, TeamViewSet, PlayerViewSet, TournamentViewSet

router = DefaultRouter()
router.register('coaches', CoachViewSet)
router.register('teams', TeamViewSet)
router.register('players', PlayerViewSet)
router.register('tournaments', TournamentViewSet)

urlpatterns = router.urls
