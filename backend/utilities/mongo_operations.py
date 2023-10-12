import pymongo
import sys


class Mongo_Actions:

    def __init__(self):
        pass

    def connect_to_mongo(self):
        client = pymongo.MongoClient('mongodb://', 27017)
        return client

    def insert_json(self, item):
        client = pymongo.MongoClient('mongodb://mongodb')
        db = client["resume_db"]
        col = db["processed"]
        col.insert_one(item)
        client.close()