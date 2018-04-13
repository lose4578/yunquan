# _*_ coding:utf-8 _*_

from django.db import models

from datetime import datetime
# from apps.user_info.models import UserMessage

# Create your models here.


class Collect(models.Model):
    collect_user_id = models.IntegerField(default=0, verbose_name='用户ID')
    collect_content_id = models.IntegerField(verbose_name=u'内容原始位置')
    collect_add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.collect_content_id)
