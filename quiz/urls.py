from django.urls import path

from .views import MultiQuestionView, StudentView, SubjectView

urlpatterns = [
    path('multi-questions/', MultiQuestionView),
    path('subjects/', SubjectView),
    path('students/', StudentView),
]