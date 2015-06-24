# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_auto_20150623_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('player_id', models.IntegerField()),
                ('team_id', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('type_name', models.CharField(max_length=20)),
                ('team_name', models.CharField(max_length=30)),
            ],
        ),
    ]
