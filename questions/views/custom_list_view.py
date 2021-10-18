from questions.models.questionmodel import QuestionModel
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, TemplateView
from questions.models.area import Area
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

class CustomListView(TemplateView, LoginRequiredMixin):
    model = Area
    template_name = 'custom_list.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect ('login')
        obj_list = self.model.objects.all()

        return render(request, self.template_name, {'obj_list':obj_list})



class CustomListShowView(TemplateView, LoginRequiredMixin):
    template_name = 'custom_list_show.html'

# Create your views here.
