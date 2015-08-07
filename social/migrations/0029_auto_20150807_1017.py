# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0028_auto_20150807_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 17, 17, 14, 254614, tzinfo=utc), verbose_name='date posted'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(max_length=200, verbose_name='Write comment: '),
        ),
        migrations.AlterField(
            model_name='wallpost',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 17, 17, 14, 253614, tzinfo=utc), verbose_name='date posted'),
        ),
        migrations.AlterField(
            model_name='wallpost',
            name='post_text',
            field=models.TextField(max_length=200, verbose_name='Write wall post: '),
        ),
    ]
