# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilante', '0002_auto_20141115_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='_lat',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='_lng',
            field=models.TextField(blank=True),
        ),
    ]
