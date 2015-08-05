# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_auto_20150804_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.IntegerField(null=True, blank=True, max_length=20, verbose_name='Facebook User ID'),
        ),
    ]
