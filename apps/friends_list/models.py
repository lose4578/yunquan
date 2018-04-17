from django.db import models
from datetime import datetime

from user_info.models import UserMessage

# Create your models here.


class UserFriendsList(models.Model):
    user_id = models.ForeignKey(UserMessage, on_delete=models.deletion.CASCADE, verbose_name='用户ID')
    user_friends_list = models.IntegerField(null=False, verbose_name=u'好友列表')
    moments_add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"好友列表"
        verbose_name_plural = verbose_name

