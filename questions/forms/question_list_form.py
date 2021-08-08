from django import forms
from ..models.area import Area

class QuestionListForm(forms.Form):
    area_options = []
 
    for a in Area.objects.all():
        area_options.append(
            (str(a), str(a))
        )



    n_questions = forms.IntegerField(label='Número de questões')
    area = forms.ChoiceField(choices=area_options, label='Área')