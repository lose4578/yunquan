from django.shortcuts import render
from .models import Collect
from news.models import News
from moments.models import Moments
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import JsonResponse

# from django.utils import simplejson
# from django.core import serializers

# Create your views here.


# class QuerySetEncoder(simplejson.JSONEncoder):
#     def default(self, object):
#         try:
#             return serializers.serialize("python", object, ensure_ascii=False)
#         except:
#             return simplejson.JSONEncoder.default(self, object)
def ajax_dict(request):
    ceshi = request.GET
    ceshi2 = request.POST
    print(ceshi)
    print(ceshi2)
    # collect_content_id = request.POST.get('secondParam')
    # collect_user_id = request.POST.get('firstParam')
    name_dict = {'lala': 'ksksks'}
    return JsonResponse(name_dict)


class AddCollect(View):
    def post(self, request):
        collect_content_id = int(request.POST.get('collect_content_id'))
        collect_user_id = int(request.POST.get('collect_user_id'))
        collect_type = int(request.POST.get('collect_type'))
        result = Collect.objects.get_or_create(collect_content_id=collect_content_id,
                                               collect_user_id_id=collect_user_id,
                                               collect_type=collect_type)

        if result[1]:
            result = {'result': '收藏成功'}
            return JsonResponse(result)
            # result = simplejson.dumps(result, cls=QuerySetEncoder)
            # return HttpResponse(result)
        else:
            result = {'result': '文章已收藏'}
            return JsonResponse(result)


class FindCollect(View):
    def post(self, request):
        collect_id = int(request.POST.get('collect_id', ''))
        collect = list(Collect.objects.filter(id=collect_id))
        if collect:
            collect = collect[0]
            if collect[1] == 1:
                result = News.objects.filter(id=collect[0])
            else:
                result = Moments.objects.filter(id=collect[0])
            # result = simplejson.dumps(result, cls=QuerySetEncoder)
            # return HttpResponse(result)
        else:
            result = {'result': '内容不存在或已被删除'}
        return JsonResponse(result)


class ReturnCollect(View):
    def post(self, request):
        collect_user_id = request.POST.get('collect_user_id', '')
        id = Collect.objects.filter(collect_user_id=collect_user_id)
        if id:
            result = {'result': [], }
            for i in collect_id:
                collect = i.__dict__['collect_content_id']
                # print(request)
                result['result'].append(collect)
            return JsonResponse(result)
            # result = simplejson.dumps(result, cls=QuerySetEncoder)
            # return HttpResponse(result)
        else:
            result = {'result': '内容不存在或已被删除'}
            return JsonResponse(result)
            # result = simplejson.dumps(result, cls=QuerySetEncoder)
            # return HttpResponse(result)

