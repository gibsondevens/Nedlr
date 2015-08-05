# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0013_auto_20150805_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(max_length=4, choices=[('Good', 'Christian'), ('Bad', 'Sinner (other)'), ('Ugly', 'Super Sinner (Atheist)')], default='Good'),
        ),
    ]
