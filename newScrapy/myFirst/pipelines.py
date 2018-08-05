# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import pymongo
from scrapy.conf import settings


class MyfirstPipeline(object):

    def __init__(self):
        # 链接数据库
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.db = self.client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        #return item  # 会在控制台输出原item数据，可以选择不写


    ''' # 初始化时指定要操作的文件
def __init__(self):
     self.file = codecs.open('questions.json', 'w', encoding='utf-8')

 # 存储数据，将 Item 实例作为 json 数据写入到文件中
 def process_item(self, item, spider):
     lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
     self.file.write(lines)
     return item

 # 处理结束后关闭 文件 IO 流
 def close_spider(self, spider):
     self.file.close()
 '''



