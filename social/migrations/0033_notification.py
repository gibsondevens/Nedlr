# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0032_auto_20150807_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('notif_text', models.CharField(choices=[('Wall Post', 'Some one has posted on your Wall'), ('Comment', 'Someone has commented on your Wall Post')], max_length=40)),
                ('notif_date', models.DateTimeField(verbose_name='Notification Date')),
            ],
        ),
    ]
