# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('fb_id', models.IntegerField(blank=True, null=True)),
                ('religion', models.CharField(default='Christian', max_length=20)),
                ('bio', models.TextField(blank=True, null=True, max_length=200)),
            ],
        ),
    ]
