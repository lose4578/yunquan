from django.shortcuts import render
from .models import UserFriendsList
from django.http import JsonResponse

from django.views.generic.base import View
# Create your views here.


class AddFriend(View):
    def post(self, request):
        user_id = request.POST.get('user_id', '')
        user_friend_id = request.POST.get('user_friend_id', '')
        user_friend_list = UserFriendsList.objects.filter(user_id=user_id)
        result = user_friend_list.objects.get_or_create(collect_user_id=user_friend_id)

        if result[1]:
            result = {'result': '好友添加成功'}
            return JsonResponse(result)
        else:
            result = {'result': '好友添加失败'}
            return JsonResponse(result)


class FindFriend(View):
    def post(self, request):
        user_id = request.POST.get('user_id', '')
        user_friends_list = UserFriendsList.objects.filter(user_id=user_id)
        return JsonResponse(user_friends_list)
