from django.shortcuts import render
from .models import Collect
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
        collect_content_id = request.POST.get('collect_content_id')
        collect_user_id = request.POST.get('collect_user_id')
        result = Collect.objects.get_or_create(collect_content_id=collect_content_id, collect_user_id=collect_user_id)

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
        collect_content_id = request.POST.get('collect_content_id', '')
        collect = Collect.objects.get(collect_content_id=collect_content_id)
        if collect:
            result = collect
            return JsonResponse(result)
            # result = simplejson.dumps(result, cls=QuerySetEncoder)
            # return HttpResponse(result)
        else:
            result = {'result': '内容不存在或已被删除'}
            return JsonResponse(result)


class ReturnCollect(View):
    def post(self, request):
        collect_content_id = request.POST.get('collect_content_id', '')
        collect_id = Collect.objects.filter(collect_content_id=collect_content_id)
        if collect_id:
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

