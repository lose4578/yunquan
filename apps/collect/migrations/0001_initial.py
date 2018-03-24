# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-24 15:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_id', models.IntegerField(default=0, verbose_name='收藏id')),
                ('collect_content_id', models.IntegerField(verbose_name='内容原始位置')),
                ('collect_add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
    ]
