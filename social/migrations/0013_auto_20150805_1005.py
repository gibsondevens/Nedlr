# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_auto_20150804_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='religion',
            field=models.CharField(max_length=4, default='Good', choices=[('Good', 'Christian'), ('Bad', 'Sinner (other)'), ('Ugly', 'Super Sinner (Atheist')]),
        ),
    ]
