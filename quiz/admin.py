from django.contrib import admin

# Register your models here.
from .models import Question, Subject, Option

admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Option)