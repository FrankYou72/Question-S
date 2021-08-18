from django.urls import path

from .views.home_view import HomeView
from .views.question_list_view import QuestionListView, QuestionListShowView
from .views.sample_question_view import SampleAreaView, SampleThemeView, SampleQuestionView
from .views.custom_list_view import CustomListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('question-list/', QuestionListView.as_view(), name='question-list'),
    path('list-show/<int:pk>', QuestionListShowView.as_view(), name='list-show'),
    path('sample', SampleAreaView.as_view(), name='sample-area'),
    path('sample/<area>', SampleThemeView.as_view(), name='sample-theme'),
    path('sample/<area>/<tema>', SampleQuestionView.as_view(), name='sample-question'),
    path('custom', CustomListView.as_view(), name='custom'),
]