from src.common.Database import Database
from src.models.Order import OrderConstants


class Order:

    def __init__(self, first_name, last_name, address, postcode, suburb, _id, time_created, item_list):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.postcode = postcode
        self.suburb = suburb
        self._id = _id
        self.time_created = time_created
        self.item_list = item_list

    def json(self):
        return {"email": self._id,
                "time_created": self.time_created,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "address": self.address,
                "postcode": self.postcode,
                "suburb": self.suburb,
                "items": self.item_list}

    def save_to_db(self):
        Database.insert(OrderConstants.COLLECTION, self.json())

    @classmethod
    def get_by_id(cls, email):
        order = Database.find_one(OrderConstants.COLLECTION, {"email": email})
        cls._id = order["email"]
        cls.first_name = order["first_name"]
        cls.last_name = order["last_name"]
        cls.address = order["address"]
        cls.postcode = order["postcode"]
        cls.suburb = order["suburb"]
        cls.item_list = order["items"]
        return cls

    # ADMIN ONLY
    @staticmethod
    def get_all():
        orders = Database.find(OrderConstants.COLLECTION, {})
        return orders
