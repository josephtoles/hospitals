# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150516_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='State',
            new_name='state',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='county_name',
            field=models.CharField(max_length=20),
        ),
    ]
