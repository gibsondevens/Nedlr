# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0022_remove_profile_fb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(blank=True, unique=True, max_length=20, verbose_name='Facebook User ID', null=True),
        ),
    ]
