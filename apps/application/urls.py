from django.urls import path
from apps.application.views import ApplicationCreateAPIView, ApplicationStatusesListAPIView
urlpatterns = [
    path("application-create/", ApplicationCreateAPIView.as_view()),
    path("application-status/", ApplicationStatusesListAPIView.as_view()),
]
