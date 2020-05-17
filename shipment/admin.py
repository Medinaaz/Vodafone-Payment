from django.contrib import admin
from shipment.models import Shipment, BillInformation

# Register your models here.
@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "surname", "email", "phone", "city", "district", "neighborhood", "others", "extra")

@admin.register(BillInformation)
class BillInformationAdmin(admin.ModelAdmin):
    list_display = ("user","name_b", "surname_b", "email_b", "phone_b", "city_b", "district_b", "neighborhood_b", "others_b")