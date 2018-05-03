# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime
from user_info.models import UserMessage
# Create your models here.

class Moments(models.Model):
    moments_id = models.IntegerField(null=False, verbose_name=u'说说id')
    moments_user = models.ForeignKey(UserMessage,verbose_name=u'用户')
    moments_text = models.TextField(verbose_name=u'说说正文')
    moments_img = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100)
    moments_like = models.IntegerField(verbose_name=u'点赞数')
    moments_comment = models.TextField(verbose_name=u'评论')
    moments_add_time = models.DateTimeField(default=datetime.now)
    user_friends_id = models.TextField(null=True, verbose_name=u"用户好友ID")

    class Meta:
        verbose_name = u"用户说说信息"