# _*_coding=utf-8

from datetime import datetime

from django.db import models
from collect.models import Collect
# Create your models here.


class UserMessage(models.Model):
    user_id = models.IntegerField(default=0,verbose_name='序号')
    user_name = models.CharField(max_length=20, default="", verbose_name=u"用户名")
    user_email = models.EmailField(verbose_name=u"邮箱")
    user_address = models.CharField(max_length=100, verbose_name=u"联系地址")
    user_birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    user_gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='female', verbose_name=u"性别")
    user_mobile = models.CharField(max_length=11, null=True, blank=True)
    user_img = models.ImageField(upload_to='image/%Y/%m', default=u"image/default.png", max_length=100)
    user_add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    user_passwd = models.CharField(max_length=50, verbose_name=u'登录密码')
    user_collect = models.ForeignKey(Collect, on_delete=models.deletion.CASCADE,verbose_name='用户收藏')

    class Meta:
        verbose_name = u"个人信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user_name



