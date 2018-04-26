# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-26 19:17
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collect_id', models.IntegerField(default=0, verbose_name='数据id')),
                ('collect_content_id', models.IntegerField(default=0, verbose_name='内容id')),
                ('collect_type', models.IntegerField(choices=[(1, '新闻'), (2, '说说')], default=1, verbose_name='收藏类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('collect_user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
    ]
