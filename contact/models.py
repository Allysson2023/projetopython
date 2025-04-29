from django.db import models
from django.utils import timezone
 
# Create your models here.
class Entrega(models.Model):
    apt = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    fotos = models.ImageField(blank=True, upload_to='entregas/%Y/%m/')
    data = models.DateTimeField(default=timezone.now)
    receberam = models.BooleanField( blank=True)

    def __str__(self) -> str:
        return self.nome

class Ocorrencia(models.Model):
    data = models.DateTimeField(default=timezone.now)
    ocorrencia = models.TextField(blank=True)
    nomeResp = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.nomeResp