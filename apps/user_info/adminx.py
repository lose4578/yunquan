import xadmin
from .models import UserMessage

class UserMessageAdmin(object):
    pass

xadmin.site.register(UserMessage,UserMessageAdmin)