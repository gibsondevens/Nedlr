# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0035_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notif_text',
            field=models.CharField(choices=[('Some one has posted on your Wall', 'Wall Post'), ('Someone has commented on your Wall Post', 'Comment')], max_length=40),
        ),
    ]
