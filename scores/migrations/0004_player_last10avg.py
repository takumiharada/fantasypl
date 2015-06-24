# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0003_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='last10avg',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
