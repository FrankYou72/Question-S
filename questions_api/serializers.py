from rest_framework import serializers

from questions.models.questionmodel import QuestionModel
from questions.models.area import Area

class QuestionModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionModel
        fields = '__all__'

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'