from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import QuestionModelSerializer, AreaSerializer, CustomSerializer
from questions.models.questionmodel import QuestionModel, Question
from questions.models.area import Area
from questions.models.custom import CustomList
from rest_framework.response import Response
from services import custom_list


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

class CustomListViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = ()
    authentication_classes = ()

    queryset = CustomList.objects.all()
    serializer_class = CustomSerializer

    def post(self, request):

        model_list = request.data['modelList']

        question_list = custom_list(model_list)

        return Response(question_list)
            





# Create your views here.
