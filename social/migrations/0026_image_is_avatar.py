# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0025_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_avatar',
            field=models.BooleanField(default=False),
        ),
    ]
