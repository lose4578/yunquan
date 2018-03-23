# _*_ coding:utf-8 _*_

from datetime import datetime

from user_info.models import UserMessage
from django.db import models
# Create your models here.


class News(models.Model):
    news_id = models.IntegerField(default=0, verbose_name=u'新闻id')
    news_user = models.ForeignKey(UserMessage, verbose_name=u'用户')
    news_name = models.CharField(max_length=30, verbose_name=u'新闻标题')
    news_text = models.TextField(verbose_name=u'新闻内容（文字）')
    news_img = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)
    news_add_time = models.DateTimeField(default=datetime.now)
    
    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.news_name
