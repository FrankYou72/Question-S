from django.shortcuts import redirect, render
from django.views.generic.base import RedirectView
from rest_framework import viewsets, permissions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .serializers import QuestionModelSerializer, AreaSerializer, CustomQuerySerializer
from questions.models.questionmodel import QuestionModel, Question
from questions.models.area import Area
from questions.models.custom import CustomList, CustomQuery
from rest_framework.response import Response
from .custom_list import get_custom


class QuestionModelViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
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


class AreaViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
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


class CustomQueryViewSet(viewsets.ModelViewSet, LoginRequiredMixin):
    permission_classes = (permissions.IsAuthenticated,)
    permission_classes = ()
    authentication_classes = ()

    queryset = CustomQuery.objects.all()
    serializer_class = CustomQuerySerializer

    
    def create(self, request):

        print('user: ', request.user)
        model_list = request.data['modelList']

        question_list = get_custom(model_list)
        ql = CustomList()
        ql.enunciados = question_list['questions']
        ql.gabaritos = question_list['answers']

        if request.user.id != None:
            ql.user_id = request.user.id
            print('user detected! - saving')
            ql.save()

        return Response(question_list)
            





# Create your views here.
