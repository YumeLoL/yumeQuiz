from django.urls import path

from .views import MultiQuestionView, SubjectView

urlpatterns = [
    path('multi-questions/', MultiQuestionView),
    path('subjects/', SubjectView),
]