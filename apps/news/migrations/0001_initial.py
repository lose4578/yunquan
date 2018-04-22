# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-22 16:01
from __future__ import unicode_literals

import ckeditor.fields
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
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_id', models.IntegerField(default=201804221601, verbose_name='新闻id')),
                ('news_name', models.CharField(max_length=30, verbose_name='新闻标题')),
                ('news_text', ckeditor.fields.RichTextField(verbose_name='新闻内容')),
                ('news_img', models.ImageField(default='image/default.png', null=True, upload_to='image/%Y/%m', verbose_name='新闻封面')),
                ('news_add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
                ('news_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
    ]
