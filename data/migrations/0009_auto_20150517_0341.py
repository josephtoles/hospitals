# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_hospital_coordinates_unknown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='provider_id',
            field=models.IntegerField(unique=True),
        ),
    ]
