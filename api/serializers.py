from rest_framework import serializers
from .models import KiharuBnd, KiharuHealthFacilitiesCleaned


class KiharuBndSerializer(serializers.ModelSerializer):
    class Meta:
        model = KiharuBnd
        geo_field = "geom"
        fields = "__all__"


class KiharuHealthFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = KiharuHealthFacilitiesCleaned
        geo_field = "geom"
        fields = "__all__"