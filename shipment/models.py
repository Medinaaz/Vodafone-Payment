from user.models import User
from typing import Union
from django.db import models
from django.db.models import Avg
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Shipment(models.Model):
    name = models.CharField(verbose_name='name', max_length=60, default='')
    surname = models.CharField(verbose_name='surname', max_length=60, default='')
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    phone = models.CharField(verbose_name='phone', max_length=60, unique=True)
    city = models.CharField(verbose_name='city', max_length=60, default='')
    district = models.CharField(verbose_name='district', max_length=60, default='')
    neighborhood = models.CharField(verbose_name='neighborhood', max_length=60, default='')
    others = models.CharField(verbose_name='others', max_length=100, default='')

    REQUIRED_FIELDS = ['phone', 'name', 'surname', 'district', 'city','email']
    field_order = {"name", "surname", "email", "phone", "city", "district", "neighborhood", "others",}
    class Meta:
        verbose_name = _("shipment")
        verbose_name_plural = _("shipments")
    def __str__(self) -> str:
        return self.name
