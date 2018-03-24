import xadmin
from .models import Collect

class CollectAdmin(object):
    pass

xadmin.site.register(Collect,CollectAdmin)