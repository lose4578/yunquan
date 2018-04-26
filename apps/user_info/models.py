# _*_coding=utf-8

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser  # 继承原有字段

# Create your models here.


class UserMessage(AbstractUser):
    user_id = models.IntegerField(default=0, verbose_name='用户ID', null=False)
    user_birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    user_gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='female')
    user_address = models.CharField(max_length=100, verbose_name=u"联系地址", null=True)
    user_mobile = models.CharField(max_length=11, null=True, blank=True)
    user_img = models.ImageField(upload_to='image/%Y/%m', default=u"image/default.png", max_length=100)
    user_iflock = models.IntegerField(default=False, verbose_name='退出是否锁定')

    class Meta:
        verbose_name = u"个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):  # 邮箱验证码
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(verbose_name='验证码类型', choices=(("register", '注册'), ('forget', '找回密码')), max_length=10)
    send_time = models.DateTimeField(verbose_name='发送时间', default=datetime.now)  # now() 程序编译时间 now class实例化时间

    class Meta:
        verbose_name = '邮箱验证码'  # 显示出来的
        verbose_name_plural = verbose_name  # 不加此句 上面会显示复数形式

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):  # 轮播图
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')  # 轮播图顺序
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
