# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0019_auto_20150805_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(max_length=20, blank=True, null=True, unique=True, default=0.5821861351377763, verbose_name='Facebook User ID'),
        ),
    ]
