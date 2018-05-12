# _*_ coding=utf-8 _*_
__author__ = 'SRF'
__date__ = '2018/4/8 21:07'
from django import forms


# 验证
class VerifyForm(forms.Form):
    code = forms.CharField(required=True)
    password = forms.CharField(required=True)


# 注册
class RegisterForm(forms.Form):
    email = forms.EmailField(required=False)
    user_mobile = forms.CharField(required=False)
    username = forms.CharField(required=True)


# 登录
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


# 忘记密码
class SendCodeForm(forms.Form):
    email = forms.EmailField(required=False)
    user_mobile = forms.CharField(required=False)


# 修改密码
class ModifyPwdForm(forms.Form):
    oldpwd = forms.CharField(required=True, min_length=5)
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


# 修改个人信息
class ModifyMessageForm(forms.Form):
    username = forms.CharField(required=False, max_length=20)
    email = forms.EmailField(required=False)
    user_address = forms.CharField(required=False, max_length=100)
    user_birday = forms.DateField(required=False, )
    user_gender = forms.CharField(required=False, max_length=10)
    user_mobile = forms.CharField(required=False, max_length=11)
    user_img = forms.CharField(required=False, max_length=100)
    user_desc = forms.CharField(required=False)
    user_signature = forms.CharField(required=False)
    user_department = forms.CharField(required=False)
