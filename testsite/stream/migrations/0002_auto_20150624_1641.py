# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20150624_1641'),
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='photo',
            field=models.ForeignKey(blank=True, to='items.PhotoItem', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stream',
            name='tweet',
            field=models.ForeignKey(blank=True, to='items.TweetItem', null=True),
            preserve_default=True,
        ),
    ]
