# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class JdcommentPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host,port=port,)
        db = client[dbname]
        self.post = db[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        postItem = dict(item)
        self.post.insert(postItem)
        return item
