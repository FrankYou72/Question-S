from questions.models.questionmodel import QuestionModel
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView
from questions.models.area import Area

class AreaListView(ListView):
    model = Area
    template_name = 'areas.html'

class AreaQuestionsView(ListView):

    def get(self, request, pk):
        model = Area
        instance = model.objects.get(area=pk)
        theme_list  = instance.questionmodel_set.all()
        return render(request, 'temas.html', {
            'theme_list' : theme_list,
            'instance':instance
            })
    
    template_name = 'temas.html'


# Create your views here.
