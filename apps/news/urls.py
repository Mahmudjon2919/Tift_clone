from .views import NewsContentListAPIView, NewsContentDetailAPIView
from django.urls import path


urlpatterns=[
    path("news/", NewsContentListAPIView.as_view()),
    path("news/<str:slug>/", NewsContentDetailAPIView.as_view())
]