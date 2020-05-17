from django.contrib import admin
from shipment.models import Shipment
# Register your models here.


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("address_id", "user", "name", "surname", "email", "phone", "city", "district", "neighborhood", "others", "extra")

