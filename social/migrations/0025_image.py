# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import social.models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0024_auto_20150805_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to=social.models.Image.make_pic_dir)),
                ('profile', models.ForeignKey(to='social.Profile')),
            ],
        ),
    ]
