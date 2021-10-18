from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(generic.TemplateView, LoginRequiredMixin):
    template_name = 'home.html'


# Create your views here.
