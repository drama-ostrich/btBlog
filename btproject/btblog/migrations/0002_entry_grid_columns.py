# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='grid_columns',
            field=models.IntegerField(default=4, null=True, blank=True),
            preserve_default=True,
        ),
    ]
