# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-24 15:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_id', models.IntegerField(default=0, verbose_name='新闻id')),
                ('news_name', models.CharField(max_length=30, verbose_name='新闻标题')),
                ('news_text', models.TextField(verbose_name='新闻内容（文字）')),
                ('news_img', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
                ('news_add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('news_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.UserMessage', verbose_name='用户')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
    ]
