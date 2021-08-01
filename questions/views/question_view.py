from django.shortcuts import render
from django.views.generic import ListView
from questions.models.questionmodel import QuestionModel


class QuestionsView(ListView):
    model = QuestionModel
    template_name = 'temas.html'


# Create your views here.
