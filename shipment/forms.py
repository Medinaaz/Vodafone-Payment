from django import forms
from shipment.models import Shipment


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["name", "surname", "email", "phone", "city", "district", "neighborhood", "others",]
    field_order = {"name", "surname", "email", "phone", "city", "district", "neighborhood", "others",}
