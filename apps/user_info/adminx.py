import xadmin
from .models import UserMessage
from xadmin.plugins.auth import UserAdmin
from xadmin import views
class UserMessageAdmin(object):
    list_display=['user_name','user_email','user_gender','user_add_time']
    search_fields=['user_name','user_id','user_gender','user_add_time']
    list_filter=['user_name','user_id','user_gender','user_add_time']

# class UserMessageAdmin(UserAdmin):
#     pass

#以下代码为后台管理系统的主题，logo配置代码

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title='云圈后台管理系统'
    site_footer='第四组'
    menu_style='accordion'


xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

