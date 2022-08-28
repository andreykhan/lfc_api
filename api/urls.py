from django.urls import path, include
from rest_framework import routers
from .views import PlayersViewSet, CoachesViewSet


router = routers.DefaultRouter()
router.register('players', PlayersViewSet),
router.register('coaches', CoachesViewSet)

urlpatterns = [
    path('', include(router.urls), name='api-root'),
]
