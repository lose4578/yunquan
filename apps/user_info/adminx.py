import xadmin
from .models import VerifyRecord,Banner
from xadmin.plugins.auth import UserAdmin
from xadmin import views
from crispy_forms.layout import Fieldset
from xadmin.layout import Main, Row, Side
from django.utils.translation import ugettext as _


#以下代码为后台管理系统的主题，logo配置代码

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title='云圈后台管理系统'
    site_footer='第四组'
    menu_style='accordion'

class VerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']      #显示列表
    search_fields = ['code', 'email', 'send_type']      #搜索
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']  # 显示列表
    search_fields = ['title', 'image', 'url', 'index']  # 搜索
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(VerifyRecord, VerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

