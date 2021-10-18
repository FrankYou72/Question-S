from questions.models.questionmodel import QuestionModel
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView, CreateView, detail
from questions.models.area import Area, QuestionList
from questions.models.questionmodel import QuestionModel
from ..forms.question_list_form import QuestionListForm

class QuestionListView(ListView):
    model = Area

    def get(self, request):
    # if this is a POST request we need to process the form data
        form = QuestionListForm()
        return render(request, 'questions_list.html', {'form': form})

    def post(self, request):
        form = QuestionListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Form is valid')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            n = form.cleaned_data['n_questions']
            area = form.cleaned_data['area']
            area_obj = self.model.objects.get(area=area)
            questions_list = area_obj.get_list(abs(int(n)))
            questions_list.user_id = request.user.id
            if request.user.id != None:
                print("FUCK")
                questions_list.save()
            print('yay')
            return QuestionListShowView().get(request,
                                                questions_list.area.area,
                                                questions_list.enunciados,
                                                questions_list.gabarito
                                                )
            
        else:
            print('Form is not valid')
            return HttpResponse('Form is not valid')

class QuestionListShowView(DetailView):
    model = QuestionList
    template = 'questions-list-show.html'
    context_object_name = 'question_list'

    def get(self, request, area, problems, answers):
        #instance = self.model.objects.get(pk=pk)
        #word_doc = instance.to_docx()
        #texts = instance.enunciados
        #answers = instance.gabarito
        #area = self.model.objects.get(pk=pk).area.area
        url = self.template
        return render(request, url, context = {
                                                'area' : area,
                                                #'pk': pk,
                                                'enunciados': problems,
                                                'gabarito':answers
                                                })
    

# Create your views here.
