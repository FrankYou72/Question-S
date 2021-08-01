from django.shortcuts import render
from rest_framework import viewsets

from .serializers import QuestionModelSerializer, AreaSerializer
from questions.models.questionmodel import QuestionModel
from questions.models.area import Area


class QuestionModelViewSet(viewsets.ModelViewSet):
    queryset = QuestionModel.objects.all()
    serializer_class = QuestionModelSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


# Create your views here.
