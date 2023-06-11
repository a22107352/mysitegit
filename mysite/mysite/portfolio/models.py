from django.db import models


# Create your models here.
class WebScrapping(models.Model):

    anos = models.IntegerField()
    obitos = models.IntegerField()
