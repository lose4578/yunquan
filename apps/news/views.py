from django.shortcuts import render
from django.db import connection
from datetime import datetime
from aip import AipNlp
from django.http import JsonResponse
from django.views.generic import View

from news.models import News
# Create your views here.

class BaiDuSDK():
    def Text_Categories(self, _title, _content):
        APP_ID = '11082811'
        API_KEY = '8UoMrydDQDuWxClQLgh3HDAt'
        SECRET_KEY = 'CDUQyIpBC8ssom0TRdKBkBpdn8Dho5VE'
        client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

        """ 调用文章分类 """
        title = _title
        content = _content
        result = client.topic(title, content)['item']
        categories = {'lv1': [], 'lv2': []}
        for i in result['lv1_tag_list']:
            if i['score'] > 0.8:
                categories['lv1'].append(i['tag'])
        for i in result['lv2_tag_list']:
            if i['score'] > 0.8:
                categories['lv2'].append(i['tag'])
        if categories['lv1'] == [] and categories['lv2'] == []:
            categories['lv1'] = False
            categories['lv2'] = False


class ShowNewsView(View):
    def post(self, request):
        click_num = int(request.POST.get('click_num'))
        news = News.objects.all().order_by('news_id')[10*(click_num-1):10 * click_num]
        news_names = []
        news_users = []
        news_texts = []
        news_imgs = []
        for i in news:
            new = News.objects.get(news_id= click_num)
            news_names = new.news_name
            news_users = new.news_user.username
            news_texts = new.news_text
            news_imgs = new.news_img
        result = {
        'news_names': news_names,
        'news_users': news_users,
        'news_texts': news_texts,
        'news_imgs': news_imgs
        }
        return JsonResponse(result)


class NewsSearch(View):
    def post(self,request):
        search = request.POST.get('search', '')#接
        with connection.cursor() as cursor:
            cursor.execute("SELECT news_id FROM news_news WHERE news_name OR news_text LIKE '%%%s%%'"%search)
            result=cursor.fetchall()
        return JsonResponse(result[0][0])

