from django.shortcuts import render
from django.views import generic

class HomeView(generic.TemplateView):
    template_name = 'home.html'


# Create your views here.
