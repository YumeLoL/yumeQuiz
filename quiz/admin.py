from django.contrib import admin

# Register your models here.
from .models import MultiQuestion, Subject
admin.site.register(MultiQuestion)
admin.site.register(Subject)