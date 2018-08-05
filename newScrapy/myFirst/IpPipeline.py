import json
import codecs
import pymongo
from scrapy.conf import settings


class IpPipeline(object):
    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.ip = self.db[settings['MONGO_IP']]  # 获得collection的句柄

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.ip.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写