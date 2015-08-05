# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_auto_20150805_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(null=True, default=None, verbose_name='Facebook User ID', unique=True, max_length=20, blank=True),
        ),
    ]
