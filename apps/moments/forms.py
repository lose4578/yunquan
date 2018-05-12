# _*_ coding:utf-8 _*_
__author__ = 'Traly'
__date__ = '2018/5/7 20:52'

from django import forms


class AddMomentsForm(forms.Form):
    moments_text = forms.CharField(required=True, max_length=150)