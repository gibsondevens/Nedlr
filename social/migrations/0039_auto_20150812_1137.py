# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0038_notification_notif_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notif_type',
            field=models.CharField(max_length=10, choices=[('Wall Post', 'Wall Post'), ('Comment', 'Comment')]),
        ),
    ]
