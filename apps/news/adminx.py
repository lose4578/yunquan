import xadmin
from .models import News
from xadmin import views
class NewsAdmin(object):
    pass

xadmin.site.register(News,NewsAdmin)