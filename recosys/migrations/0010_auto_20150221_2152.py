# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recosys', '0009_auto_20150211_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealRate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rate', models.FloatField()),
                ('movie', models.ForeignKey(to='recosys.Movie')),
                ('user', models.ForeignKey(to='recosys.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuggestRate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rate', models.FloatField()),
                ('movie', models.ForeignKey(to='recosys.Movie')),
                ('user', models.ForeignKey(to='recosys.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='avg_rate',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='avg_rate2',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='watched_users',
        ),
        migrations.RemoveField(
            model_name='user',
            name='n_movies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rated',
        ),
        migrations.RemoveField(
            model_name='user',
            name='watched',
        ),
    ]
