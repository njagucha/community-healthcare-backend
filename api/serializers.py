from rest_framework import serializers
from .models import KiharuBnd, KiharuHealthFacilitiesCleaned, Landmarks
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


class KiharuBndSerializer(serializers.ModelSerializer):
    class Meta:
        model = KiharuBnd
        geo_field = "geom"
        fields = "__all__"


class KiharuHealthFacilitiesSerializer(serializers.ModelSerializer):
    landmarks_within_500M = serializers.SerializerMethodField()

    def get_landmarks_within_500M(self, obj):
        landmark_location = Point(obj.longitude, obj.latitude, srid=4326)
        query = Landmarks.objects.filter(geom__distance_lte=(landmark_location, 500))
        query_serialized = LandmarkSerializer(query, many=True)
        return query_serialized.data
    class Meta:
        model = KiharuHealthFacilitiesCleaned
        geo_field = "geom"
        fields = "__all__"

class LandmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landmarks
        geo_field = "geom"
        fields = "__all__"