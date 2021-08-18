from questions.models.questionmodel import QuestionModel
from questions.models.area import Area

def get_themes(area):
    area_obj = Area.objects.get(area=area)
    qm_objs = QuestionModel.objects.filter(area=area_obj)
    themes = []

    for q in qm_objs:
        themes.append(q.tema)

    return themes
