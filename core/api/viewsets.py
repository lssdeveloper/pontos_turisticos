from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all() #lista todos os pontos turisticos
    serializer_class = PontoTuristicoSerializer  #quais os campos quero mostrar

    def list(self, request, *args, **kwargs):
        return Response({'teste': 123})

    def create(self, request, *args, **kwargs):
        return Response({'Helo': request.data['nome']})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    @action(methods=['get'], detail=True)           #decorator
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass

 #   def get_queryset(self):
 #       return PontoTuristico.objectes.filter(aprovado=True)