from django.db import models
from multiselectfield import MultiSelectField
import datetime

from django.db import models
from django.utils import timezone


class Subject(models.Model):
    subject_text = models.CharField('Quiz Subject', max_length=100)

    def __str__(self):
        return '<%s:%s>' % (self.subject_text, 'Subject')

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
        return '<%s:%s>' % (self.question_text, 'Quiz Question')

class Student(models.Model):
    sid = models.BigAutoField('Student Id', primary_key=True, default=None)
    name = models.CharField('Student Name', max_length=200, unique=True, default=None)
    age = models.IntegerField('Student Age', default=0)
    gender = models.BooleanField('Gender',choices=((0,'female'),(1,'male')), default=0)
    pwd = models.CharField('Password',max_length=20, default=None)

    def __str__(self):
        return '<%s:%s>' % (self.name, 'Student Name')


class Record(models.Model):
    sid = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='Student Id',related_name='stu_id')
    score = models.IntegerField('Score', default=0)
    rtime = models.DateTimeField('Submit Time:',blank=True,null=True)

    def __str__(self):
        return '<%s:%s>' % (self.sid, 'Score')