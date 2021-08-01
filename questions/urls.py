from django.urls import path

from .views.area_view import AreaQuestionsView
from .views.home_view import HomeView
from .views.question_list_view import QuestionListView, QuestionListShowView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('question-list/', QuestionListView.as_view(), name='question-list'),
    path('list-show/<int:pk>', QuestionListShowView.as_view(), name='list-show'),
]