from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all() #lista todos os pontos turisticos
    serializer_class = PontoTuristicoSerializer  #quais os campos quero mostrar