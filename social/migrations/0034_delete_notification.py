# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0033_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
