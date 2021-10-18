from django.contrib.auth.mixins import LoginRequiredMixin
from questions.models.questionmodel import QuestionModel
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, TemplateView
from questions.models.area import Area

class ContactView(TemplateView):
    template_name = 'contact.html'
