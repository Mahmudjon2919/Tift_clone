from django.urls import path
from apps.common.views import RegionListAPIView, DistrictListByRegionAPIView, SocialListAPIView, GenderChoicesAPIView

urlpatterns = [
    path('regions/', RegionListAPIView.as_view),
    path('<int:pk>/districts/', DistrictListByRegionAPIView.as_view()),
    path('socials/', SocialListAPIView.as_view()),
    path('genders/', GenderChoicesAPIView.as_view())
]

