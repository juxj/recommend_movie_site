# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recosys', '0012_user_watched_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rated_users',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
