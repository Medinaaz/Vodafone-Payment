from django.urls import path

from shipment.views import save_shipment, confirm_shipment, change_shipment

urlpatterns = [
    path('confirm/', confirm_shipment, name="confirm_shipment"),
    path('change/', change_shipment, name="change_shipment"),
    path('', save_shipment, name="save_shipment"),
]
