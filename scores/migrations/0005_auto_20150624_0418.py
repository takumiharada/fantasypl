# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0004_player_last10avg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='last10avg',
            new_name='last10minutes',
        ),
        migrations.AddField(
            model_name='player',
            name='last10total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='totalminutes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='totalpoints',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
