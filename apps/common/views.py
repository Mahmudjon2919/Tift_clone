from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.common.models import Region, District, Social
from apps.common.serializer import RegionListSerializer


class RegionListAPIView(generics.ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()

