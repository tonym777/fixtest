import pymongo


class MongoDBAPI:

    def __init__(self):
        self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.mongo_client["fix"]
        self.collection = self.db["fix_orders"]

    def insert(self, order):
        self.collection.insert_one(order)
