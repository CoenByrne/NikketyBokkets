from src.common.Database import Database
from src.models.Review.ReviewConstants import COLLECTION
import uuid


class Review(object):
    def __init__(self, item_id, title, rating, content, _id=None):
        self.itemID = item_id
        self.title = title
        self.rating = rating
        self.content = content
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_db(self):
        Database.insert(COLLECTION, self.json())

    def json(self):
        return {
            "_id": self._id,
            "item_id": self.itemID,
            "rating": str(self.rating),
            "title": self.title,
            "content": self.content
            }

    @classmethod
    def find_by_product_id(cls, item_id):
        return cls(**Database.find(COLLECTION, {"item_id": item_id}))
