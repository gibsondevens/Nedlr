# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0029_auto_20150807_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_date',
        ),
        migrations.RemoveField(
            model_name='wallpost',
            name='post_date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=200, verbose_name='Write comment'),
        ),
        migrations.AlterField(
            model_name='wallpost',
            name='post_text',
            field=models.TextField(max_length=200, verbose_name='Write wall post'),
        ),
    ]
