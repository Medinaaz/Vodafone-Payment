from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, View
from django.shortcuts import render
from shipment.models import Shipment
from product.models import Product, StatusChoices
from django.http import JsonResponse
from django import forms
from shipment.forms import ShipmentForm, BillInformationForm


def confirm_shipment(request):
    form = ShipmentForm(request.POST)
    bill_form = BillInformationForm(request.POST)
    return render(request,'confirm_delivery.html', {'form': form , 'bill_form': bill_form})  #


def change_shipment(request):
    form = ShipmentForm()
    if request.method == "POST":
        form = ShipmentForm(request.POST)
    else:
        form = ShipmentForm()
    bill_form = save_bill(request)
    return render(request, 'delivery.html', {'form': form, 'bill_form': bill_form})


def save_shipment(request):
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():

            shipment_form = form.save(commit=False)
            shipment_form.user = request.user
            shipment_form.save()

    else:

        form = ShipmentForm()

    bill_form = save_bill(request)

    return render(request, 'delivery.html', {'form': form, 'bill_form': bill_form})  #


def save_bill(request):
    if request.method == "POST":
        form = BillInformationForm(request.POST)
        if form.is_valid():
            bill_form = form.save(commit=False)
            bill_form.user = request.user
            bill_form.save()
    else:
        bill_form = BillInformationForm()

    return bill_form