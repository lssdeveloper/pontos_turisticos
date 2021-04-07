from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all() #lista todos os pontos turisticos
    serializer_class = AvaliacaoSerializer  #quais os campos quero mostrar