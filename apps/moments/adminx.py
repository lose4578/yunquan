import xadmin
from .models import Moments
from xadmin import views
class MomentsAdmin(object):
    pass

xadmin.site.register(Moments,MomentsAdmin)