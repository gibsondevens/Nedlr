# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0026_image_is_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('poster_id', models.IntegerField()),
                ('comment_text', models.TextField(max_length=200)),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 2, 9, 40, 612705, tzinfo=utc), verbose_name='date posted')),
            ],
        ),
        migrations.CreateModel(
            name='WallPost',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('poster_id', models.IntegerField()),
                ('post_text', models.TextField(max_length=200)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 2, 9, 40, 611705, tzinfo=utc), verbose_name='date posted')),
                ('profile', models.ForeignKey(to='social.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='social.WallPost'),
        ),
    ]
