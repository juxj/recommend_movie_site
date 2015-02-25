# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recosys', '0011_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watched_movies',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
