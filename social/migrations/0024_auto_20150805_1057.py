# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0023_profile_fb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.BigIntegerField(unique=True, verbose_name='Facebook User ID', blank=True, null=True),
        ),
    ]
