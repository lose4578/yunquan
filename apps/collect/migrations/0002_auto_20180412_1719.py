# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-12 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='collect_id',
        ),
        migrations.AddField(
            model_name='collect',
            name='collect_user_id',
            field=models.IntegerField(default=0, verbose_name='用户ID'),
        ),
    ]
