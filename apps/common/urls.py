from django.urls import path
from .views import RegionListAPIView

urlpatterns = [
    path('regions/', RegionListAPIView.as_view(), name='region-list'),
]
