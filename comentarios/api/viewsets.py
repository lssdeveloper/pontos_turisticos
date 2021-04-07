from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()  # lista todos os pontos turisticos
    serializer_class = ComentarioSerializer