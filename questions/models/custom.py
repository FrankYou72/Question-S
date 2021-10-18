from typing import List, Tuple
from django.db import models
from django.db.models import manager,CASCADE, ForeignKey, JSONField
from django.db.models.fields import CharField, TextField, DateTimeField
from django.contrib.auth.models import User


class CustomList(models.Model):
    criado = DateTimeField(auto_now=True)
    enunciados = JSONField()
    gabaritos = JSONField()
    user = ForeignKey(User, on_delete=CASCADE, null=True)

    def __str__(self):
        return 'custom'+ str(self.criado) + '/'



class CustomQuery(models.Model):
    modelList = JSONField()


# Create your models here.
