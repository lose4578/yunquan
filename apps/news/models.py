# _*_ coding:utf-8 _*_
from ckeditor.fields import RichTextField
from datetime import datetime
from user_info.models import UserMessage
from django.db import models
import time as _time


# Create your models here.


class News(models.Model):
    news_id = models.CharField(verbose_name=u'新闻 id',default = _time.time,max_length=20)
    news_user = models.ForeignKey(UserMessage,on_delete=models.deletion.CASCADE,verbose_name=u'用户')
    news_name = models.CharField(max_length=30, verbose_name=u'新闻标题')
    news_text = RichTextField(verbose_name="新闻内容")
    news_img = models.ImageField(verbose_name="新闻封面",null=True,upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)
    news_add_time = models.DateTimeField(verbose_name="上传时间",default = datetime.now)

    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.news_name