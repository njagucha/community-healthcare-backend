from django.contrib.gis.db import models


# Create your models here.
class KiharuBnd(models.Model):
    fid = models.BigIntegerField(blank=True, null=True)
    id_0 = models.BigIntegerField(blank=True, null=True)
    iso = models.CharField(max_length=3, blank=True, null=True)
    name_0 = models.CharField(max_length=75, blank=True, null=True)
    id_1 = models.BigIntegerField(blank=True, null=True)
    name_1 = models.CharField(max_length=75, blank=True, null=True)
    id_2 = models.BigIntegerField(blank=True, null=True)
    name_2 = models.CharField(max_length=75, blank=True, null=True)
    hasc_2 = models.CharField(max_length=15, blank=True, null=True)
    ccn_2 = models.BigIntegerField(blank=True, null=True)
    cca_2 = models.CharField(max_length=254, blank=True, null=True)
    type_2 = models.CharField(max_length=50, blank=True, null=True)
    engtype_2 = models.CharField(max_length=50, blank=True, null=True)
    nl_name_2 = models.CharField(max_length=75, blank=True, null=True)
    varname_2 = models.CharField(max_length=150, blank=True, null=True)
    geom = models.MultiPolygonField(blank=True, null=True)

    class Meta:
        db_table = "kiharu_bnd"
        verbose_name_plural = "Kiharu Bnd"


class KiharuHealthFacilitiesCleaned(models.Model):
    class Services(models.TextChoices):
        PRIMARY_CARE = "Primary Care", "Primary Care"
        DENTAL = "Dental", "Dental"
        MATERNAL_HEALTH = "Maternal Health", "Maternal Health"
        IMMUNIZATION = "Immunization", "Immunization"
        LABORATORY_SERVICES = "Laboratory Services", "Laboratory Services"

    class Amenities(models.TextChoices):
        PHARMACY = "Pharmacy", "Pharmacy"
        RESTROOM = "Restroom", "Restroom"
        WAITING_AREA = "Waiting Area", "Waiting Area"
        PLAY_GROUND = "Play Ground", "Play Ground"

    no = models.IntegerField(blank=True, null=True)
    county = models.CharField(blank=True, null=True)
    sub_county = models.CharField(db_column="sub county", blank=True, null=True)
    name_of_health_facility = models.CharField(
        db_column="name of health facility", blank=True, null=True
    )
    mfl_number = models.IntegerField(db_column="mfl number", blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    contact = models.CharField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)
    picture1 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture2 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture3 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture4 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture5 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    services_offered = models.CharField(max_length=255, blank=True, null=True)
    facility_type_choices = (
        ("Public", "Public"),
        ("Private", "Private"),
    )
    facility_type = models.CharField(
        max_length=100, blank=True, null=True, choices=facility_type_choices
    )
    road_accessibility = models.BooleanField(default=True)
    adequate_parking = models.BooleanField(default=True)
    electricity = models.BooleanField(default=True)
    clean_water = models.BooleanField(default=True)
    wheelchair_accessible = models.BooleanField(default=True)
    community_healthcare_programs = models.BooleanField(default=True)
    emergencies = models.BooleanField(default=True)
    operating_hrs = models.CharField(max_length=200, blank=True, null=True)
    healthcare_professionals = models.IntegerField(blank=True, null=True)
    amenities_available = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "kiharu_health_facilities_cleaned"
        verbose_name_plural = "Kiharu Health Facilities"

    def __str__(self):
        return self.name_of_health_facility

    def get_services_display(self):
        services_list = self.services_offered.split(",")
        return ", ".join([self.Services(service).label for service in services_list])

    def get_amenities_display(self):
        amenities_list = self.amenities_available.split(",")
        return ", ".join([self.Amenities(amenity).label for amenity in amenities_list])


class Landmarks(models.Model):
    name = models.CharField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    geom = models.PointField(blank=True, null=True)

    class Meta:
        db_table = "landmarks"
        verbose_name_plural = "Landmarks"

    def __str__(self):
        return self.name
