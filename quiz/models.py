from django.db import models
import datetime

from django.db import models
from django.utils import timezone


class Subject(models.Model):
    subject_text = models.CharField(
        max_length=100, verbose_name='Quiz Subject')

    def __str__(self):
        return self.subject_text


class Question(models.Model):
    TYPE_CHOICES = ((0, 'Single Answer'),
                    (1, 'Multi Answer'))

    category = models.ForeignKey(
        Subject, on_delete=models.CASCADE, blank=True, null=True)
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Quiz Type', default=0)
    question_text = models.CharField(
        max_length=200, verbose_name='Question', blank=False, null=False)
   

    # add __str__() methods to your models to represent objects’ names
    def __str__(self):
        return self.question_text


class Option(models.Model):
    OPTION_CHOICES = (
        (1, 'A'),
        (2, 'B'),
        (3, 'C'),
        (4, 'D'),
    )

    options = models.IntegerField(choices=OPTION_CHOICES, verbose_name='Option: ABCD')
    content = models.CharField(max_length=256, verbose_name='选项内容')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content