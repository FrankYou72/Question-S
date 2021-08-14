from questions.models.questionmodel import QuestionModel
from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, TemplateView
from questions.models.area import Area

class SampleAreaView(TemplateView):
    model=Area
    template_name = 'sample_area'

    def get(self, request):
        area_list = self.model.objects.all()
        return render(request, 'sample_question_area.html' , {'areaList': area_list})

class SampleThemeView(TemplateView):
    model=QuestionModel
    template_name = 'sample_theme'

    def get(self, request, area):
        area_obj = Area.objects.get(area=area)
        theme_list = self.model.objects.filter(area=area_obj)
        return render(request, 'sample_question_theme.html' , {'themeList': theme_list, 'area':area})

class SampleQuestionView(TemplateView):
    model=QuestionModel
    template_name = 'sample_theme'

    def get(self, request, area, tema):
        theme_obj = self.model.objects.get(tema=str(tema))

        question = theme_obj.get_question()
        return render(request, 'sample_question.html' , {
                                                                'theme': tema,
                                                                'area':area,
                                                                'pergunta': question.enunciado,
                                                                'resposta': question.gabarito
                                                                })


#class SampleThemeView(DetailView):
#    model = QuestionList
#    template = 'questions-list-show.html'
#    context_object_name = 'question_list'
#
#    def get(self, request, pk):
#        instance = self.model.objects.get(pk=pk)
#        texts = instance.enunciados
#        answers = instance.gabarito
#        area = self.model.objects.get(pk=pk).area.area
#        url = self.template
#        return render(request, url, context = {'area' : area, 'pk': pk, 'enunciados': texts, 'gabarito':answers})
#
#
#class SampleQuestionView(DetailView):
#    model = QuestionList
#    template = 'questions-list-show.html'
#    context_object_name = 'question_list'
#
#    def get(self, request, pk):
#        instance = self.model.objects.get(pk=pk)
#        texts = instance.enunciados
#        answers = instance.gabarito
#        area = self.model.objects.get(pk=pk).area.area
#        url = self.template
#        return render(request, url, context = {'area' : area, 'pk': pk, 'enunciados': texts, 'gabarito':answers})
#
#
## Create your views here.
#