from questions.models.questionmodel import QuestionModel
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, TemplateView
from questions.models.area import Area

class CustomListView(TemplateView):
    model = Area
    template_name = 'custom_list.html'

    def get(self, request):
        obj_list = self.model.objects.all()

        return render(request, self.template_name, {'obj_list':obj_list} )


# Create your views here.
