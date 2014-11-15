# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilante', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='lat',
            new_name='_lat',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='lng',
            new_name='_lng',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='endreco',
            new_name='endereco',
        ),
    ]
