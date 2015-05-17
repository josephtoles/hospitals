# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20150517_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='coordinates_unknown',
            field=models.BooleanField(default=False),
        ),
    ]
