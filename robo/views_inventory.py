from .models import Inventory
from .serializers import InventorySerializer
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
