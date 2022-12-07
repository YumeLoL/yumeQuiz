from django.contrib import admin

from .models import MultiQuestion, Student, Subject

# Register your models here.
admin.site.register(MultiQuestion)
admin.site.register(Subject)
admin.site.register(Student)
