from django.db import models
from django.db.models import manager,CASCADE, ForeignKey, JSONField
from django.db.models.fields import CharField, TextField
from random import choice

class Area(models.Model):
    area = CharField(max_length = 100)
    objects = manager.Manager()

    def get_list(self, n):
        temas  = self.questionmodel_set.all()
        question_list = {
            'questões': {},
            'gabarito': {}
        }
        
        for i in range(n):
            q_model = choice(temas)
            question = q_model.get_question()
            question_list['questões'][str(i+1)] = question.enunciado
            question_list['gabarito'][str(i+1)] = question.gabarito

        return QuestionList(area=self, enunciados = question_list['questões'], gabarito = question_list['gabarito'])

    def __str__(self):
        return self.area

class QuestionList(models.Model):
    area = ForeignKey(Area, on_delete=CASCADE)
    enunciados = JSONField()
    gabarito = JSONField()
