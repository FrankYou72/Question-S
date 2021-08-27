from questions.models.area import Area, QuestionList
from questions.models.questionmodel import QuestionModel, Question
from questions.models.custom import CustomList


def get_custom(model_list):

    custom_list = {
        'questions':[],
        'answers': []
    }

    for model in model_list:
        print(model)
        area = Area.objects.get(area=model['area'])
        question_model = QuestionModel.objects.filter(area=area, tema=model['theme'])[0]
        question = question_model.get_question()
        custom_list['questions'].append(question.enunciado)
        custom_list['answers'].append(question.gabarito)

    return custom_list
