# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20150804_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fb_access_token',
        ),
    ]
