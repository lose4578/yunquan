# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default='', verbose_name='序号')),
                ('user_id', models.IntegerField(default=0, verbose_name='序号')),
                ('user_name', models.CharField(default='', max_length=20, verbose_name='用户名')),
                ('user_email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('user_address', models.CharField(max_length=100, verbose_name='联系地址')),
                ('user_birday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('user_gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10)),
                ('user_mobile', models.CharField(blank=True, max_length=11, null=True)),
                ('user_img', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
                ('user_add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user_passwd', models.CharField(max_length=50, verbose_name='登录密码')),
                ('user_collect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collect.Collect', verbose_name='用户收藏')),
            ],
            options={
                'verbose_name': '个人信息',
                'verbose_name_plural': '个人信息',
            },
        ),
    ]
