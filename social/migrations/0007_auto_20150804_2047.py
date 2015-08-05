# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20150804_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_user_id',
            field=models.CharField(verbose_name='Facebook User ID', max_length=20, null=True, blank=True),
        ),
    ]
