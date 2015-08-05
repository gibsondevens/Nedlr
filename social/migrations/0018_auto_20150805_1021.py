# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_auto_20150805_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(default='Christian', max_length=22, choices=[('Christian', 'Christian'), ('Sinner (other)', 'Sinner (other)'), ('Super Sinner (Atheist)', 'Super Sinner (Atheist)')]),
        ),
    ]
