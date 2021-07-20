from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    telegramID = models.CharField(max_length=8,blank=True,null=True)
    telegramUser = models.CharField(max_length=10,blank=True,null=True)


class Estrategia(models.Model):
    nome = models.CharField(max_length=30,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    apm = models.FloatField(null=True)
    gols = models.IntegerField(null=True)
    escanteios = models.IntegerField(null=True)


    def __str__(self):
        return self.nome

    class Meta:
        order_with_respect_to = 'user'