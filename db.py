import pymongo


class MongoDB:
    def __init__(self, db_name, col_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[col_name]

    def insert_data_list(self, data):
        return self.collection.insert_many(data)

    def get_data(self):
        return self.collection.find()

