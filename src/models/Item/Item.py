from src.models.Item import ItemConstants
from src.common.Database import Database
import uuid


class Item:
    
    def __init__(self, title, description, size, category, price, _id=None):
        self.title = title
        self.description = description
        self.size = size
        self.category = category
        self.price = price
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "_id": self._id,
            "title": self.title,
            "description": self.description,
            "size": self.size,
            "category": self.category,
            "price": str(self.price)
            }

    def save_to_db(self):
        Database.insert(ItemConstants.COLLECTION, self.json())

    def from_db(self):
        Database.find_one(ItemConstants.COLLECTION, {"title": self.title})

    @staticmethod
    def get_by_id(item_id):
        return Database.find_one(ItemConstants.COLLECTION, {"_id": item_id})

    @classmethod
    def get_by_name(cls, name):
        return Database.find(ItemConstants.COLLECTION, {"title": name})

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find(ItemConstants.COLLECTION, {})]

    @staticmethod
    def all_from_category(category):
        return Database.find(ItemConstants.COLLECTION, {"category": category})
