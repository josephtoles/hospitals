# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150516_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='atmosphere',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='quality',
            field=models.FloatField(null=True),
        ),
    ]
