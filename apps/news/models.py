# _*_ coding:utf-8 _*_

from datetime import datetime
from DjangoUeditor.models import UEditorField
from user_info.models import UserMessage
from django.db import models


# Create your models here.


class News(models.Model):
    news_id = models.IntegerField(verbose_name=u'新闻id')
    news_user = models.ForeignKey(UserMessage, on_delete=models.deletion.CASCADE,verbose_name=u'用户')
    news_name = models.CharField(max_length=30, verbose_name=u'新闻标题')
    news_text = UEditorField(verbose_name=u"新闻内容", width=600, height=300, imagePath="courses/ueditor/", filePath="courses/ueditor/",default='')
    news_img = models.ImageField(null=True,upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)
    news_add_time = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = "新闻"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.news_name


