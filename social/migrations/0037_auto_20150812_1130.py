# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0036_auto_20150812_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notif_text',
            field=models.CharField(max_length=40),
        ),
    ]
