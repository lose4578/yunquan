import xadmin
from .models import UserMessage
from xadmin.plugins.auth import UserAdmin
from xadmin import views
from crispy_forms.layout import Fieldset
from xadmin.layout import Main, Row, Side
from django.utils.translation import ugettext as _
# class UserMessageAdmin(object):
#     list_display=['user_name','user_email','user_gender','user_add_time']
#     search_fields=['user_name','user_id','user_gender','user_add_time']
#     list_filter=['user_name','user_id','user_gender','user_add_time']

class UserMessageAdmin(UserAdmin):
    def get_form_layout(self):
        self.form_layout = (
            Main(
                Fieldset('',
                         'username', 'password',
                         css_class='unsort no_title'
                         ),
                Fieldset(_('Personal info'),
                         Row('first_name', 'last_name'),
                         'email'
                         ),
                Fieldset(_('Permissions'),
                         'groups', 'user_permissions'
                         ),
                Fieldset(_('Important dates'),
                         'last_login', 'date_joined'
                         ),
            ),
            Side(
                Fieldset(_('Status'),
                         'is_active',  'is_superuser',
                         ),
            )
        )
        return super(UserAdmin, self).get_form_layout()

#以下代码为后台管理系统的主题，logo配置代码

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title='云圈后台管理系统'
    site_footer='第四组'
    menu_style='accordion'

# xadmin.site.unregister(UserMessage)
# xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

