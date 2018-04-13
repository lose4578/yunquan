# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='user_gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10, verbose_name='性别'),
        ),
    ]
