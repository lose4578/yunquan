from django.views.generic import View
from django.http import JsonResponse
from django.db import connection
import re
import time
import json

from function import format

from .forms import AddMomentsForm
from .models import Moments
from user_info.models import UserMessage
from friends_list.models import UserFriendsList
# Create your views here.


class AddMomentsView(View):
    def post(self, request):
        moments_user = int(request.POST.get('user_id'))
        moments_text = request.POST.get('text')
        moments_img = request.POST.get('img')
        moments = Moments()
        user = UserMessage.objects.get(id = moments_user)
        moments.moments_user = user
        moments.moments_text = moments_text
        moments.moments_img = moments_img
        moments.save()
        result = {'result': '说说发表成功！'}
        return JsonResponse(result)


class ShowMomentsView(View):
    def post(self, request):
        moments_user = int(request.POST.get('user_id'))
        moments = Moments.objects.filter(moments_user_id = moments_user)
        moments_users = []
        moments_texts = []
        moments_likes = []
        for i in moments:
            moments_user = moments[i].moments_user
            moments_text = moments[i].moments_text
            moments_like = moments[i].moments_like
            moments_users += moments_user
            moments_texts += moments_text
            moments_likes += moments_like


        # user_message = list(user_message)
        # user_message = format(user_message)
        friends_list = UserFriendsList.objects.filter(user_id = moments_user)
        # all_friend_moments = []
        # for n in friend_ids:
        #     friend_moments = Moments.objects.filter(moments_user = friend_ids[n])
        #     friend_moments = list(friend_moments)
        #     friend_moments = format(friend_moments)
        #     friend_moments = list(friend_moments.values())
        #     all_friend_moments += friend_moments
        #
        # moments = Moments.objects.filter(moments_user = moments_user)
        # moments = list(moments)
        # moments = format(moments)
        # moments = list(moments.values())
        # moments += all_friend_moments
        # for i in moments:
        #     for j in range(0, len(moments)-1):
        #         add_time1 = moments[j]['add_time']
        #         add_time2 = moments[j+1]['add_time']
        #         timeArray1 = time.strptime(add_time1, "%Y-%m-%d %H:%M:%S")
        #         timeArray2 = time.strptime(add_time2, "%Y-%m-%d %H:%M:%S")
        #         timestamp1 = time.mktime(timeArray1)
        #         timestamp2 = time.mktime(timeArray2)
        #         if timestamp1 > timestamp2:
        #             temp = moments[j]
        #             moments[j] = moments[j+1]
        #             moments[j+1] = temp


        result = {
            'moments_users': moments_users,
            'moments_texts': moments_texts,
            'moments_likes': moments_likes,
        }
        return JsonResponse(result)


class LikeView(View):
    def post(self, request):
        moments_id = request.POST.get("moments_id")
        moment = Moments.objects.get(id = moments_id)
        moment.moments_like += 1
        moment.save()
        like_num = moment.moments_like
        result = {'like_num': like_num}
        return JsonResponse(result)


class AddCommentView(View):
    def post(self, request):
        moments_id = int(request.POST.get('moments_id'))
        comment_user_id = int(request.POST.get('user_id'))
        user = UserMessage.objects.get(id = comment_user_id)
        comment_user_name = user.username
        comment = request.POST.get('comment')
        comment = comment_user_name + '``' + comment + '~~'
        moment = Moments.objects.get(id = moments_id)
        moment.moments_comment += comment
        moment.save()
        return JsonResponse({
            'result': '评论成功！'
        })


class ShowCommentView(View):
    def post(self, request):
        moments_id = int(request.POST.get('moments_id'))
        moment = Moments.objects.get(id= moments_id)
        all_comments = moment.moments_comment
        users = re.findall('~~([\s\S]*?)``', all_comments)
        comments = re.findall('``([\s\S]*?)~~', all_comments)
        return JsonResponse({
            'users': users,
            'comments': comments
        })
    
class MomentsSearch(View):
    def post(self,request):
        search = request.POST.get('search', '')#接
        id = request.POST.get('id', '')#接
        with connection.cursor() as cursor:
            cursor.execute("SELECT moments_id FROM moments_moments WHERE moments_user_id=%d AND moments_text LIKE '%%%s%%'"%(int(id),search))
            result=cursor.fetchall()
        return JsonResponse(result[0][0])
