from django.urls import path
from .views import SingleResumeParser,BatchResumeParser

urlpatterns = [
    path('parse/', SingleResumeParser.as_view(), name='parse-resume'),
    path('parse-multiple/', BatchResumeParser.as_view(), name='batch-parse'),
]