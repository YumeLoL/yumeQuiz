from django.urls import path

from .views import MultiQuestionView, RecordView, StudentView, SubjectView

urlpatterns = [
    path('multi-questions/', MultiQuestionView),
    path('subjects/', SubjectView),
    path('students/', StudentView),
    path('records/', RecordView),
]