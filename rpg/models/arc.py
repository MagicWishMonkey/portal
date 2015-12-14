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



class ARC(models.Model):
    class Meta:
        app_label = 'rpg'
        db_table = 'ARC'

    id = AutoField(primary_key=True)
    label = CharField(null=True, blank=True, max_length=1000)


    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)
    label = CharField(null=True, blank=True, max_length=1000)

    date_created = DateTimeField(auto_now=True)