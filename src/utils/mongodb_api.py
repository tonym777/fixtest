import pymongo


class MongoDBAPI:

    def __init__(self):
        self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.mongo_client["fix"]

    def insert_one(self, collection_name, record):
        collection = self.db[collection_name]
        collection.insert_one(record)

    def insert_many(self, collection_name, records):
        collection = self.db[collection_name]
        collection.insert_many(records)

    def update_one(self, collection_name, filter, update):
        collection = self.db[collection_name]
        collection.update_one(filter, update)

    def update_many(self, collection_name, filter, update):
        collection = self.db[collection_name]
        collection.update_many(filter, update)

    def delete_one(self, collection_name, filter):
        collection = self.db[collection_name]
        collection.delete_one(filter)

    def delete_many(self, collection_name, filter):
        collection = self.db[collection_name]
        collection.delete_many(filter)
