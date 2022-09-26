import json
import random

import requests
import urllib3
from faker import Faker

urllib3.disable_warnings()


# class MyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         """
#         只要检查到了是bytes类型的数据就把它转为str类型
#         :param obj:
#         :return:
#         """
#         if isinstance(obj, bytes):
#             return str(obj, encoding='utf-8')
#         return json.JSONEncoder.default(self, obj)


class Param:
    def __init__(self, username, age, sex, nickName, address):
        self.username = username
        self.age = age
        self.sex = sex
        self.nickName = nickName
        self.address = address

    # def __repr__(self):
    #     return repr((self.username, self.age, self.sex, self.nickName, self.address))


if __name__ == '__main__':
    sexs = ['男', '女']
    # db = pymysql.connect(host="152.136.225.78", user="root", password="123456", database="test_vue_01")
    # cursor = db.cursor()
    fake = Faker("zh_CN")
    locs = ['北京', '天津', '河北', '山西', '内蒙古', '湖南', '湖北', '辽宁', '吉林', '上海', '深圳', '江苏', '浙江', '广东', '重庆', '海南', '台湾']

    for i in range(1000):
        # 准备随机数据
        index = random.randint(0, 1)
        sex = sexs[index]
        username = fake.name()
        nick_name = username
        address = locs[random.randint(0, len(locs) - 1)]
        age = random.randint(10, 50)

        # 封装json对象
        params = Param(username, age, sex, nick_name, address)
        json_params = json.dumps(params, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
        # print(params.__dict__)
        # print(json_params)

        # 发送请求
        headers = {"Content-Type": "application/json", "Transfer-Encoding": "chunked"}
        resp = requests.post("http://localhost:9090/user", json=params.__dict__)
        # print(resp)
