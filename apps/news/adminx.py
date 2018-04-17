import xadmin
from .models import News
from xadmin import views
class NewsAdmin(object):
    list_display=['news_name','news_id','news_user']
    search_fields=['news_name','news_id']
    list_filter=['news_name','news_id','news_user']

xadmin.site.register(News,NewsAdmin)