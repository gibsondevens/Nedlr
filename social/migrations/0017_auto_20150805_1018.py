# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0016_auto_20150805_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fb_id',
            field=models.CharField(verbose_name='Facebook User ID', null=True, max_length=20, blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(choices=[('Christian', 'Christian'), ('Sinner (other)', 'Sinner (other)'), ('Super Sinner (Atheist)', 'Super Sinner (Atheist)')], max_length=4, default='Christian'),
        ),
    ]
