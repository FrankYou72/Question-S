from questions.models.area import Area, QuestionList
from questions.models.questionmodel import QuestionModel, Question


def get_custom(model_list):

    custom_list = {
        'questions':[],
        'answers': []
    }

    for model in model_list:
        area = Area.objects.get(area=model['area'])
        question_model = QuestionModel.objects.filter(area=area, tema=model['tema'])[0]
        question = question_model.get_question()
        custom_list['questions'].append(question.enunciado)
        custom_list['answers'].append(question.gabarito)

    return(custom_list)
