# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 20:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='collect_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
