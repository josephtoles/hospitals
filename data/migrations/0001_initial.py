# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider_id', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('quality', models.FloatField()),
                ('atmosphere', models.FloatField()),
                ('cost', models.FloatField()),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=10)),
                ('zip_code', models.IntegerField()),
                ('county_name', models.IntegerField()),
            ],
        ),
    ]
