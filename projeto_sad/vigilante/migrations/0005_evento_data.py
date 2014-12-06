# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilante', '0004_evento_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='data',
            field=models.DateField(default='2012-05-21'),
            preserve_default=False,
        ),
    ]
