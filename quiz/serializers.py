from django.forms import TypedChoiceField
from rest_framework import serializers
from .models import MultiQuestion, Record, Student, Subject

class MultiQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiQuestion
        fields =['category', 'type','question_text', 'answer']
        #  ['optionA', 'optionB', 'optionC', 'optionD'],

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields =['subject_text']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['sid','name','age','gender','pwd']

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields =['sid','score','rtime']
    