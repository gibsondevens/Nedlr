# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0027_auto_20150806_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(verbose_name='date posted', default=datetime.datetime(2015, 8, 7, 17, 14, 49, 328325, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='wallpost',
            name='post_date',
            field=models.DateTimeField(verbose_name='date posted', default=datetime.datetime(2015, 8, 7, 17, 14, 49, 327325, tzinfo=utc)),
        ),
    ]
