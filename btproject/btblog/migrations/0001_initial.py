# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'TX', max_length=2, choices=[(b'IM', b'Image'), (b'SI', b'Small Img'), (b'TX', b'Text'), (b'ST', b'Status'), (b'AU', b'Audio'), (b'VI', b'Video'), (b'EV', b'Event')])),
                ('title', models.CharField(max_length=255, blank=True)),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('text', models.TextField(blank=True)),
                ('width', models.IntegerField(null=True, blank=True)),
                ('height', models.IntegerField(null=True, blank=True)),
                ('audio', models.FileField(null=True, upload_to=b'upload', blank=True)),
                ('video', models.FileField(null=True, upload_to=b'upload', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'upload', blank=True)),
                ('order_manual', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
            bases=(models.Model,),
        ),
    ]
