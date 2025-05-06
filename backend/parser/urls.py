from django.urls import path
from .views import ResumeParseView,ResumeParseBatchView
from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [ path('parse/', ResumeParseView.as_view()) ,
#                path('parse-multiple/', BatchResumeParseView.as_view(), name='parse-multiple'),
#                ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from django.urls import path
# from .views import ResumeParseView, ResumeParseBatchView

urlpatterns = [
    path('parse/', ResumeParseView.as_view(), name='parse-single'),
    path('parse-multiple/', ResumeParseBatchView.as_view(), name='parse-multiple'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)