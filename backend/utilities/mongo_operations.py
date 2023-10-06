import pymongo
import sys


class Mongo_Actions:

    def __init__(self):
        pass



    def connect_to_mongo(self):
        client = pymongo.MongoClient('mongodb://clusterAdmin:admin123@docdb-2023-10-06-14-07-17.cyywauqyq9p5.ap-south-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false')
        return client

    def insert_json(self, item):
        client = self.connect_to_mongo()
        db = client["resume_db"]
        col = db["processed"]
        col.insert_one(item)
        client.close()