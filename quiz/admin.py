from django.contrib import admin

from .models import MultiQuestion, Record, Student, Subject

# Register your models here.
admin.site.register(MultiQuestion)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Record)
