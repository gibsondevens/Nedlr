# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0037_auto_20150812_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notif_type',
            field=models.CharField(choices=[('Wall Post', 'Wall Post'), ('Comment', 'Comment')], max_length=10, default='Wall Post'),
        ),
    ]
