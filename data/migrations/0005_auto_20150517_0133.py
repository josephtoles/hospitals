# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20150516_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestsRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='hospital',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]
