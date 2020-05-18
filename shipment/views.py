from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, View
from django.shortcuts import render
from shipment.models import Shipment
from product.models import Product, StatusChoices
from django.http import JsonResponse
from django import forms
from shipment.forms import ShipmentForm


def confirm_shipment(request):
    form = ShipmentForm(request.POST)
    return render(request,'confirm_delivery.html', {'form': form})


def change_shipment(request):
    form = ShipmentForm()
    if request.method == "POST":
        form = ShipmentForm(request.POST)
    else:
        form = ShipmentForm()
    return render(request, 'delivery.html', {'form': form})


def save_shipment(request):
    form = ShipmentForm()
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment_form = form.save(commit=False)
            shipment_form.save()
    else:
        form = ShipmentForm()
    return render(request, 'delivery.html', {'form': form})

