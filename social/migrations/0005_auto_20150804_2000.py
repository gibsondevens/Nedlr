# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_remove_profile_fb_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_user_id',
            field=models.TextField(null=True, blank=True, verbose_name='Facebook User ID'),
        ),
    ]
