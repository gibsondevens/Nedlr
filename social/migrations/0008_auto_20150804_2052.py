# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20150804_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fb_user_id',
            new_name='fb_id',
        ),
    ]
