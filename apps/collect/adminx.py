import xadmin
from .models import Collect
from xadmin import views
class CollectAdmin(object):
    pass

xadmin.site.register(Collect,CollectAdmin)