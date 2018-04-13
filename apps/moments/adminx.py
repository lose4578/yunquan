import xadmin
from .models import Moments
from xadmin import views
class MomentsAdmin(object):
    list_display=['moments_like','moments_id','moments_user']
    search_fields=['moments_like','moments_id','moments_user']
    list_filter=['moments_like','moments_id','moments_user']

xadmin.site.register(Moments,MomentsAdmin)