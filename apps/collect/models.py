# _*_ coding:utf-8 _*_

from django.db import models

from datetime import datetime

from django.db import models
from user_info.models import UserMessage


# Create your models here.


class Collect(models.Model):
    collect_user_id = models.ForeignKey(UserMessage, verbose_name='用户',on_delete=models.CASCADE)  # 一条数据是一个内容 ，同一个用户可有多条
    collect_id = models.IntegerField(default=0, verbose_name='数据id')
    collect_content_id = models.IntegerField(default=0, verbose_name=u'内容id')
    collect_type = models.IntegerField(choices=((1, "新闻"), (2, "说说")), default=1, verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = u'收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.collect_content_id)
