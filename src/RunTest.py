from flask import session

from src.models.Item.Item import Item
from src.models.Review.Review import Review
from src.models.ShoppingCart import ShoppingCartConstants
from src.models.User.User import User
from src.common.Database import Database
from src.models.User import UserConstants
from src.models.Item import ItemConstants
from src.models.Review import ReviewConstants
from src.models.ShoppingCart.ShoppingCart import ShoppingCart

Database.initialize()

print(ShoppingCart.find_by_user_id("f0a46fd4725f47dbb47ab6b214c67060"))

items = Item.all_from_category("1")
for item in items:
    print(item)
