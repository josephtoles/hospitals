from django.db import models
from django.db.models import IntegerField, CharField, FloatField


class Hospital(models.Model):
    provider_id = IntegerField()  # Used by Medicare. Distinct from database primary key.
    phone_number = IntegerField()

    # Metrics
    quality = FloatField(null=True)
    atmosphere = FloatField(null=True)
    price = FloatField(null=True)

    # Address
    name = CharField(max_length=100)
    address = CharField(max_length=100)
    city = CharField(max_length=20)
    state = CharField(max_length=10)
    zip_code = IntegerField()
    county_name = CharField(max_length=20)

    # Coordinates
    lat = FloatField(null=True)
    lng = FloatField(null=True)

    def __unicode__(self):
        return self.name or 'anonymous'


class RequestsRecord(models.Model):
    date = models.DateField(unique=True)
    requests = IntegerField()