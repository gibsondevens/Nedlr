# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0030_auto_20150807_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='poster_username',
            field=models.CharField(max_length=20, default='PaulRudd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wallpost',
            name='poster_username',
            field=models.CharField(max_length=20, default='PaulRudd'),
            preserve_default=False,
        ),
    ]
