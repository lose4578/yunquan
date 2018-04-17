import xadmin
from .models import News
from xadmin import views
class NewsAdmin(object):
    list_display=['news_name','news_id','news_user']
    search_fields=['news_name','news_id']
    list_filter=['news_name','news_id','news_user']


class CourseAdmin(object):
    style_fields = {"news_text": "ueditor"}

xadmin.site.register(News,NewsAdmin)