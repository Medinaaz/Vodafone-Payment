from django import forms
from shipment.models import Shipment


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ["address_id", "address_name", "name", "surname", "email", "phone",
                  "city", "district", "neighborhood", "others", "extra"]

