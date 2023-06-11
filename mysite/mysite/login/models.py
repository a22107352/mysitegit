from uuid import uuid4

from django.db import models

# Create your models here.
# myapp/models.py

from django.db import models
from django.contrib.auth.models import User


class Cadeira(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    ranking = models.IntegerField()
    ects = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Projeto(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titulo
