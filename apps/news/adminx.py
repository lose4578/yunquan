import xadmin
from .models import News

class NewsAdmin(object):
    pass

xadmin.site.register(News,NewsAdmin)