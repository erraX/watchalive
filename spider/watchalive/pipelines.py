# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class WatchalivePipeline(object):
    def __init__(self):
        self.file = open('../../web/playerlist.json', 'wb')
        self.file2 = open('playerlist.json', 'wb')

    def process_item(self, item, spider): 
        line = json.dumps(dict(item), ensure_ascii=False).encode('utf8') + "\n" 
        self.file.write(line)
        self.file2.write(line)
        return item
