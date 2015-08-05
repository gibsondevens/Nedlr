# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20150804_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_user_id',
            field=models.IntegerField(verbose_name='Facebook User ID', blank=True, null=True),
        ),
    ]
