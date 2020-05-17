from django import forms
from shipment.models import Shipment, BillInformation


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["name", "surname", "email", "phone", "city", "district", "neighborhood", "others", "extra"]
    field_order = {"name", "surname", "email", "phone", "city", "district", "neighborhood", "others", "extra"}


class BillInformationForm(forms.ModelForm):
    class Meta:
        model = BillInformation
        fields = ["name_b", "surname_b", "email_b", "phone_b", "city_b", "district_b", "neighborhood_b", "others_b"]
