from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db.models import ForeignKey
from django.db.models.fields import (
    AutoField,
    CharField,
    IntegerField,
    DecimalField,
    BinaryField,
    DateTimeField
)
from .enums import Status


class Plan(models.Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'Plans'

    id = AutoField(primary_key=True)
    label = CharField(null=False, blank=False, max_length=200)

    style = ForeignKey(Status)

    stories = IntegerField(null=False, blank=False, default=1)
    bedrooms = IntegerField(null=False, blank=False, default=1)
    baths = DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    garage = IntegerField(null=False, blank=False, default=1)

    min_sqft = IntegerField(null=False, blank=False)
    max_sqft = IntegerField(null=False, blank=False)
    elevation = IntegerField(null=False, blank=False)

    date_created = DateTimeField(auto_now=True)
    date_submitted = DateTimeField(auto_now=False, null=True, blank=True)