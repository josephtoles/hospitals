from django.db import models
from django.db.models import IntegerField, CharField, FloatField


class hospital(models.Model):
    provider_id = IntegerField()  # Used by Medicare. Distinct from database primary key.
    phone_number = IntegerField()

    # Metrics
    quality = FloatField()
    atmosphere = FloatField()
    price = FloatField()

    # Address
    name = CharField(max_length=100)
    address = CharField(max_length=100)
    city = CharField(max_length=20)
    State = CharField(max_length=10)
    zip_code = IntegerField()
    county_name = IntegerField()

