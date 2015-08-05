# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20150804_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(null=True, blank=True, unique=True, verbose_name='Facebook User ID', max_length=20),
        ),
    ]
