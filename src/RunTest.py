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
from src.models.Order.Order import Order
Database.initialize()

orders = Order.get_all()
for order in orders:
    print(order["last_name"])
