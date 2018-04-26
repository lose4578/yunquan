# _*_ coding:utf-8 _*_
__author__ = 'Traly'
__date__ = '2018/4/14 12:41'

from aip import AipNlp
import json
import re


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


def format(list):
    bigdict = {}
    for i in list:
        test = re.sub('\'', '\"', str(i))
        dict = json.loads(test)
        flag = dict['id']
        bigdict[flag] = test
    return bigdict



    # 功能：
    # 将filter得到的数据库中的多条数据变为字典格式（嵌套字典）
    # 参数list为filter得到的 list化的数据
    # 大字典 键 为id
