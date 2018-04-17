import xadmin
from .models import UserFriendsList
from xadmin import views
class UserFriendsListAdmin(object):
    list_display=['news_name','news_id','news_user']
    search_fields=['user_friends_list','moments_add_time']
    list_filter=['user_friends_list','moments_add_time']

xadmin.site.register(UserFriendsList,UserFriendsListAdmin)