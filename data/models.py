from django.db import models
from django.db.models import IntegerField, CharField, FloatField


class Hospital(models.Model):
    provider_id = IntegerField(unique=True)  # Used by Medicare. Distinct from database primary key.
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
    coordinates_unknown = models.BooleanField(default=False)  # set to true of coordinate lookup fails

    def __unicode__(self):
        return self.name or 'anonymous'

    def round_quality(self):
        return int(self.quality * 100)

    def round_atmosphere(self):
        return int(self.atmosphere * 100)

    def round_price(self):
        return int(self.price * 100)


class RequestsRecord(models.Model):
    date = models.DateField(unique=True)
    requests = IntegerField()