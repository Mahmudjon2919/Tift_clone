from rest_framework import serializers
from apps.common.models import Region, District, Social



class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields=("id", "title")


class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields=("id", "title")