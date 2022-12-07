from django.db import models
from multiselectfield import MultiSelectField
import datetime

from django.db import models
from django.utils import timezone


class Subject(models.Model):
    subject_text = models.CharField('Quiz Subject', max_length=100)

    def __str__(self):
        return self.subject_text

class MultiQuestion(models.Model):
    TYPE_CHOICES = ((0, 'Single Answer'),(1, 'Multi Answer'))
    MY_CHOICES = (('A', 'A'),('B', 'B'),('C', 'C'),('D', 'D'))

    category = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    type = models.IntegerField('Quiz Type', choices=TYPE_CHOICES, default=0)
    question_text = models.CharField('Question',max_length=200,blank=False, null=False)
    
    optionA = models.CharField('A',max_length=40,default=None)
    optionB = models.CharField('B',max_length=40,default=None)
    optionC = models.CharField('C',max_length=40,default=None)
    optionD = models.CharField('D',max_length=40,default=None)

    answer = MultiSelectField('Quiz Answer', choices=MY_CHOICES, default='',max_choices=3, max_length=9)
    point = models.IntegerField('Point', default=0)

    def __str__(self):
        return self.question_text

class Student(models.Model):
    GENDER = (('female','female'), ('male','male'))
    
    name = models.CharField('Student Name', max_length=200, default='')
    age = models.IntegerField('Student Age', default=0)
    gender = models.CharField('Student Gender',choices=GENDER ,max_length=100, default='female')


    def __str__(self):
        return self.name

