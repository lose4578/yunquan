import xadmin
from .models import Collect
from xadmin import views
class CollectAdmin(object):
    list_display=['collect_content_id','collect_user_id','add_time']
    search_fields=['collect_content_id','collect_user_id','add_time']
    list_filter=['collect_content_id','collect_user_id','add_time']

xadmin.site.register(Collect,CollectAdmin)


