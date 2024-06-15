from typing import Any
from django import forms
from django.contrib import admin
from .models import KiharuBnd, KiharuHealthFacilitiesCleaned, Landmarks
from .forms import HealthFacilityForm
from leaflet.admin import LeafletGeoAdmin


# Register your models here.


class KiharuBndAdmin(LeafletGeoAdmin):
    pass


class KiharuHealthFacilitiesAdmin(LeafletGeoAdmin):
    form = HealthFacilityForm
    list_display = ("name_of_health_facility", "level")


class LandmarksAdmin(LeafletGeoAdmin):
    list_display = ("name", "type")


admin.site.register(KiharuBnd, KiharuBndAdmin)
admin.site.register(KiharuHealthFacilitiesCleaned, KiharuHealthFacilitiesAdmin)
admin.site.register(Landmarks, LandmarksAdmin)

