# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0020_auto_20150805_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(null=True, max_length=20, verbose_name='Facebook User ID', unique=True, blank=True),
        ),
    ]
