from typing import List, Tuple
from django.db import models
from django.db.models import manager,CASCADE, ForeignKey, JSONField
from django.db.models.fields import CharField, TextField, DateTimeField


class CustomList(models.Model):
    criado = DateTimeField(auto_now=True)
    enunciados = JSONField()
    gabaritos = JSONField()

    def __str__(self):
        return 'custom'+ str(self.criado) + '/'

# Create your models here.
