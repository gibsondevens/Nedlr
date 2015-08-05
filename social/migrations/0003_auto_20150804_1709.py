# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20150804_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_access_token',
            field=models.TextField(verbose_name='Facebook Access Token', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fb_user_id',
            field=models.IntegerField(verbose_name='Facebook User ID', null=True, blank=True),
        ),
    ]
