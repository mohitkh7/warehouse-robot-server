from .models import Inventory, Sample
from .serializers import InventorySerializer, SampleSerializer
from rest_framework import generics


class InventoryCreate(generics.CreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryList(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryUpdate(generics.UpdateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDelete(generics.DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class SampleCreate(generics.CreateAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
