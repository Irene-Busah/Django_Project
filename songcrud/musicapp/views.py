from rest_framework import viewsets
from .models import Artiste, Song
from django.http import JsonResponse
from .serializers import ArtisteSerializer, SongSerializer


# Create your views here.
class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
