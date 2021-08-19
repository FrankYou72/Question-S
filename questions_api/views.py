from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import QuestionModelSerializer, AreaSerializer
from questions.models.questionmodel import QuestionModel, Question
from questions.models.area import Area
from rest_framework.response import Response

class QuestionModelViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = ()
    authentication_classes = ()

    queryset = QuestionModel.objects.all()
    serializer_class = QuestionModelSerializer

    def get_queryset(self):
        """Retrieve the posts for the authenticated user"""
        print(self.request.query_params)
        area = self.request.query_params.get('area')
        area_parent = Area.objects.get(area=area)
        queryset = self.queryset
        if area:
            queryset = queryset.filter(area=area_parent)

        return queryset.all()


class AreaViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = ()
    authentication_classes = ()

    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def get_queryset(self):
        """Retrieve the posts for the authenticated user"""
        print(self.request.query_params)
        area = self.request.query_params.get('area')
        queryset = self.queryset
        if area:
            queryset = queryset.filter(area=area)

        return queryset.all()



# Create your views here.
