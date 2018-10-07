from django.contrib import admin
from .models import Warehouse, Robot, Inventory

# Register your models here.
admin.site.register(Warehouse)
admin.site.register(Robot)
admin.site.register(Inventory)
