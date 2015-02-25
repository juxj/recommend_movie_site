# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recosys', '0010_auto_20150221_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.FloatField(default=123, blank=True),
            preserve_default=True,
        ),
    ]
