from rest_framework import serializers

from questions.models.questionmodel import QuestionModel
from questions.models.area import Area
from questions.models.custom import CustomList


class QuestionModelSerializer(serializers.HyperlinkedModelSerializer):
    permission_classes = ()
    class Meta:
        model = QuestionModel
        fields = '__all__'

class AreaSerializer(serializers.HyperlinkedModelSerializer):
    permission_classes = ()
    class Meta:
        model = Area
        fields = '__all__'


class CustomSerializer(serializers.HyperlinkedModelSerializer):
    permission_classes = ()
    class Meta:
        model = CustomList
        fields = '__all__'