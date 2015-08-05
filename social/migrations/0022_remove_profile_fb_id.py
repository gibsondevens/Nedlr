# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0021_auto_20150805_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fb_id',
        ),
    ]
