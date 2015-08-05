# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='fb_id',
            new_name='fb_user_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='fb_access_token',
            field=models.TextField(null=True, blank=True),
        ),
    ]
