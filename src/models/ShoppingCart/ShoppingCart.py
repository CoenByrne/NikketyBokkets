from src.common.Database import Database
from src.models.Item.Item import ItemConstants
from src.models.ShoppingCart import ShoppingCartConstants
import uuid


class ShoppingCart:

    def __init__(self, time_created, temp, user_email=None, _id=None):
        self.time_created = time_created
        self.temp = temp
        self.user_email = uuid.uuid4().hex if user_email is None else user_email
        self._id = uuid.uuid4().hex if _id is None else _id
        self.shopping_list = []

    def add_item(self, item_id):
        self.shopping_list.append(item_id)

    def json(self):
        item_cart = {"user_email": self.user_email,
                     "_id": self._id,
                     "temp": self.temp,
                     "time_created": self.time_created,
                     "items": self.shopping_list}
        return item_cart

    def save_to_db(self):
        Database.insert(ShoppingCartConstants.COLLECTION, self.json())

    @classmethod
    def find_items(cls, cart_json):
        item_list = []
        items = cart_json["items"]
        for item_id in items:
            item_list.append(Database.find_one(ItemConstants.COLLECTION, {"_id": item_id}))
        return item_list

    @classmethod
    def find_by_user_id(cls, email):
        cart = Database.find_one(ShoppingCartConstants.COLLECTION, {"user_email": email})
        cls.user_email = cart["user_email"]
        cls.time_created = cart["time_created"]
        cls.temp = cart["temp"]
        cls._id = cart["_id"]
        cls.shopping_list = cart["items"]
        return cls
