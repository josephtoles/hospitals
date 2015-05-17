# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_requestsrecord_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestsrecord',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
