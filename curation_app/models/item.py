from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://curating_user:curating_password@localhost:27017/curating_db")
db = client['curating_db']


class Item:
    def __init__(self, content, status='pending'):
        self.content = content
        self.status = status
    
    def save(self):
        item = {
            'content': self.content,
            'status': self.status
        }
        db.items.insert_one(item)

    @staticmethod
    def get_all():
        return db.items.find()

    @staticmethod
    def get_by_id(item_id):
        return db.items.find_one({'_id': ObjectId(item_id)})

    @staticmethod
    def update_status(item_id, status):
        db.items.update_one({'_id': ObjectId(item_id)}, {'$set': {'status': status}})
