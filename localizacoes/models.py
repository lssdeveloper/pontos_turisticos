from django.db import models

# Create your models here.
class Localizacao(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True) #opcionais
    longitude = models.IntegerField(null=True, blank=True) #opcionais

    def __str__(self):
        return self.linha1
