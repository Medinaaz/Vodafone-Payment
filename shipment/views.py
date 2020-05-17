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
    return render(request, 'confirm_delivery.html', {'form': form})


def change_shipment(request):
    form = ShipmentForm()
    if request.method == "POST":
        form = ShipmentForm(request.POST)
    else:
        form = ShipmentForm()
    return render(request, 'delivery.html', {'form': form})


def add_shipment(request):
    shipment_list = []
    address_form = ShipmentForm()
    bill_form = ShipmentForm()
    ctr = 1
    for element in Shipment.objects.filter(user=request.user).values():
        print(element)
        form_element = ShipmentForm(element)
        print(form_element)
        shipment_list += [form_element]
        ctr += 1

    print(shipment_list)
    return render(request, 'add_delivery.html', {"shipment_list": shipment_list,
                                                 "address_form": address_form,
                                                 "bill_form": bill_form})


def save_shipment(request):
    if request.method == "POST":
        form = ShipmentForm(request.POST)
        if form.is_valid():

            shipment_form = form.save(commit=False)
            shipment_form.user = request.user
            shipment_form.save()

    else:
        main_dict = {}
        ctr = 1
        for element in Shipment.objects.filter(user=request.user).values():
            form_element = ShipmentForm(element)
            main_dict["shipment_form" + str(ctr)] = form_element
            ctr += 1
        print(main_dict)
        form = ShipmentForm()

    return render(request, 'delivery.html', main_dict)
