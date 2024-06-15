from rest_framework import generics
from .models import KiharuBnd, KiharuHealthFacilitiesCleaned
from .serializers import KiharuBndSerializer, KiharuHealthFacilitiesSerializer


# Create your views here.
class KiharuBndList(generics.ListAPIView):
    queryset = KiharuBnd.objects.all()
    serializer_class = KiharuBndSerializer


class KiharuHealthFacilitiesList(generics.ListAPIView):
    queryset = KiharuHealthFacilitiesCleaned.objects.all()
    serializer_class = KiharuHealthFacilitiesSerializer


class KiharuFaciltiesDetail(generics.RetrieveAPIView):
    queryset = KiharuHealthFacilitiesCleaned.objects.all()
    serializer_class = KiharuHealthFacilitiesSerializer
