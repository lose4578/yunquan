import xadmin
from .models import UserMessage
from xadmin import views
class UserMessageAdmin(object):
    pass

xadmin.site.register(UserMessage,UserMessageAdmin)