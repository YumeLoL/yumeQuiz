from django.forms import TypedChoiceField
from rest_framework import serializers
from .models import MultiQuestion, Subject

class MultiQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiQuestion
        fields =['category', 'type','question_text', 'answer']
        #  ['optionA', 'optionB', 'optionC', 'optionD'],

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields =['subject_text']
    