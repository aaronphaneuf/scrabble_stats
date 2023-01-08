from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, GameViewSet, WordViewSet, CreateWordViewSet, CreateGameViewSet

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('games', GameViewSet, basename='games')
router.register('words', CreateWordViewSet, basename='words')
router.register('addgame', CreateGameViewSet, basename='addgame')


urlpatterns = [
    path('', include(router.urls)),
]