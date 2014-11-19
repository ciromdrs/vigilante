# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilante', '0003_auto_20141115_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='tipo',
            field=models.CharField(default='ASSALTO', max_length=30, choices=[(b'ASSALTO', b'Assalto'), (b'FURTO', b'Furto'), (b'HOMICIDIO', b'Homic\xc3\xaddio'), (b'SUICIDIO', b'Suic\xc3\xaddio'), (b'DROGAS', b'Drogas')]),
            preserve_default=False,
        ),
    ]
