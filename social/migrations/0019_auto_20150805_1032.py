# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0018_auto_20150805_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(max_length=20, verbose_name='Facebook User ID', null=True, unique=True, blank=True, default=0.126429553657481),
        ),
    ]
