# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='cost',
            new_name='price',
        ),
    ]
