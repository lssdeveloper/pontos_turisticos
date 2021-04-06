from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateField(auto_now=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username

