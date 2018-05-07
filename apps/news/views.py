from django.shortcuts import render

from datetime import datetime
from aip import AipNlp
from django.http import JsonResponse

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
        news_num = request.POST.get('news_num')
        news = News.objects.order_by('news_id')[10*(news_num-1):10 * news_num]
        news_names = []
        news_users = []
        news_texts = []
        news_imgs = []
        for i in news:
            news_name = news[i].news_name
            news_user = news[i].news_user
            news_text = news[i].news_text
            news_img = news[i].news_img
            news_names += news_name
            news_users += news_user
            news_texts += news_text
            news_imgs += news_img
        return JsonResponse({
            'news_names': news_names,
            'news_users': news_users,
            'news_texts': news_texts,
            'news_imgs': news_imgs
        })






