import pymongo
import sys


class Mongo_Actions:

    def __init__(self):
        pass

    def connect_to_mongo(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)
        return client

    def insert_json(self, item):
        client = self.connect_to_mongo()
        db = client["resume_db"]
        col = db["processed"]
        col.insert_one(item)
        client.close()