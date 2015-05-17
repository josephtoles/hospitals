# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20150517_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestsrecord',
            name='requests',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
