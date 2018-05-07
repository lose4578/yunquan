# _*_ coding=utf-8 _*_
__author__ = 'SRF'
__date__ = '2018/3/29 21:07'

from random import Random
from django.core.mail import send_mail

from user_info.models import VerifyRecord
from yunquan.settings import EMAIL_FROM
from note.smsclient import SmsClient


def random_str(randomlength=4):
    str = ''
    chars = '1234567890'
    random = Random()
    length = len(chars) - 1
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_verify_code(type1, email_or_mobile, send_type):  # 发送验证码
    verify_record = VerifyRecord()
    code = random_str(4)
    verify_record.code = code
    verify_record.email_or_mobile = email_or_mobile  # 手机or邮箱
    verify_record.send_type = send_type
    verify_record.save()

    if type1 == 'email':
        email_title = "云顶APP账号{}验证码".format(send_type)
        email_body = "{}账号验证码：{}，打死都不要告诉别人哦！".format(send_type, code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email_or_mobile])
        if send_status:
            pass
    elif type1 == 'mobile':
        smsClient = SmsClient()
        smsClient.singleSend(email_or_mobile,code)
