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

    # 示例：
    # models.py
    #
    # a = {'id': self.id, 'city_id': self.city_id, 'desc': self.desc, 'name': self.name}
    # return str(a)
    #
    # views.py
    #
    # all_orgs = all_orgs.filter(city_id=int(city_id))
    # a = list(all_orgs)
    # print(format(a))

    # 输出结果：
    #
    # {1: '{"id": 1, "city_id": 2, "desc": "慕课网是垂直的互联网IT技能免费学习网站。
    # 以独家视频教程、在线编程工具、学习计划、问答社区为核心特色。在这里，你可以找到最好的互联网技术牛人，
    # 也可以通过免费的在线公开视频课程学习国内领先的互联网IT技术。\\r\\n慕课网课程涵盖前端开发、PHP、Html5
    # 、Android、iOS、Swift等IT前沿技术语言，包括基础课程、实用案例、高级分享三大类型，适合不同阶段的学习人群
    # 。以纯干货、短视频的形式为平台特点，为在校学生、职场白领提供了一个迅速提升技能、共同分享进步的学习平台。
    #  [1] \\r\\n          4月2日，国内首个IT技能学习类应用——慕课网3.1.0版本在应用宝首发。据了解，在此次
    # 上线的版本中，慕课网新增了课程历史记录、相关课程推荐等四大功能，为用户营造更加丰富的移动端IT学习体验。",
    # "name": "慕课网"}', 3: '{"id": 3, "city_id": 2, "desc": "红豆生南国，春来发几枝。\\r\\n愿君多采撷
    # ，此物最相思。", "name": "相思"}', 5: '{"id": 5, "city_id": 2, "desc": "关关雎鸠，在河之洲。窈
    # 窕淑女，君子好逑。\\r\\n参差荇菜，左右流之。窈窕淑女，寤寐求之。\\r\\n求之不得，寤寐思服。悠哉悠哉，
    # 辗转反侧。\\r\\n参差荇菜，左右采之。窈窕淑女，琴瑟友之。\\r\\n参差荇菜，左右芼之。窈窕淑女，钟鼓乐之。
    # ", "name": "关雎"}'}


    # 功能：
    # 将filter得到的数据库中的多条数据变为字典格式（嵌套字典）
    # 参数list为filter得到的 list化的数据
    # 大字典 键 为id
