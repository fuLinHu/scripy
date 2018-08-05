import requests
import pymongo
from scrapy.conf import settings
import random

class ScripyUtil(object):

    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.ip = self.db[settings['MONGO_IP']]  # 获得collection的句柄


    def judge_ip(self,ip, port):
        # 判断ip是否可用
        http_url = "http://www.xicidaili.com/nn/"
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http": proxy_url,
            }
            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            print("invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print("effective ip")
                return True
            else:
                print("invalid ip and port")
                self.delete_ip(ip)
                return False


    def delete_ip(self,ip):
        myquery = {"ip": ip}
        self.ip.delete_one(myquery)

    def get_random_ip(self):
        # 从数据库中随机获取一个可用的ip
        result = self.ip.find()
        result_list = list(result[:])
        length=len(result_list)
        randint=random.randint(0, length-1)
        resultOne=result_list[randint]
        ip=resultOne['ip']
        port = resultOne['port']
        judge_re = self.judge_ip(ip, port)
        if judge_re:
            return "http://{0}:{1}".format(ip, port)
        else:
            return self.get_random_ip()
