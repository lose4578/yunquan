# _*_coding=utf-8

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser  # 继承原有字段

# Create your models here.


class UserMessage(AbstractUser):
    user_id = models.IntegerField(default=0,verbose_name='用户ID', null=False)
    user_birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    user_gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='female')
    user_address = models.CharField(max_length=100, verbose_name=u"联系地址", null=True)
    user_mobile = models.CharField(max_length=11, null=True, blank=True)
    user_img = models.ImageField(upload_to='image/%Y/%m', default=u"image/default.png", max_length=100)
    user_iflock = models.IntegerField(default=False, verbose_name='退出是否锁定')
    user_sinature = models.CharField(default='', verbose_name='个性签名', max_length=80, null=True)
    user_desc = models.CharField(default='', verbose_name='个人描述', max_length=255, null=True)
    user_department = models.CharField(verbose_name='部门', max_length=20, choices=(("JAVA", 'JAVA'), ("Node.js", "Node.js"), ("Python", "Python"), ("Frontend", "前端"), ("others", "其他")),default='', null=True)

    class Meta:
        verbose_name = u"个人信息"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.username

class VerifyRecord(models.Model):  # 验证码
    code = models.CharField(max_length=20, verbose_name='验证码')
    email_or_mobile = models.CharField(max_length=50, verbose_name='邮箱或手机',default=0)
    send_type = models.CharField(verbose_name='验证码类型', choices=(("mobileregister", '手机注册'),("emailregister", '邮箱注册'),("mobileforget", '手机找回密码'), ('emailforget', '邮箱找回密码')), max_length=20)
    send_time = models.DateTimeField(verbose_name='发送时间', default=datetime.now)  # now() 程序编译时间 now class实例化时间

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email_or_mobile)


class Banner(models.Model):  # 轮播图
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')  # 轮播图顺序
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
