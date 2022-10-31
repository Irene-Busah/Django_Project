from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtisteViewSet, SongViewSet

router = DefaultRouter()
router.register('artistes', ArtisteViewSet, basename='artistes')
router.register('songs', SongViewSet, basename='songs')

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + router.urls
