from flask import Blueprint, render_template, request, session

from src.common.Database import Database
from src.models.ShoppingCart import ShoppingCartConstants
from src.models.ShoppingCart.ShoppingCart import ShoppingCart

shopping_cart_blueprint = Blueprint("ShoppingCart", __name__)


@shopping_cart_blueprint.route("/cart", methods=['GET', 'POST'])
def too_cart():
    if request.method == 'GET':
        if "email" in session.keys():
            cart = Database.find_one(ShoppingCartConstants.COLLECTION, {"user_email": session["email"]})
            items = ShoppingCart.find_items(cart)
            return render_template("shopping_cart.html", items=items)
        return render_template("shopping_cart.html")


@shopping_cart_blueprint.route("/cart", methods=['GET', 'POST'])
def empty_cart():
    return render_template("shopping_cart.html")


@shopping_cart_blueprint.route("/remove", methods=['POST'])
def remove_item():
    cart = Database.find_one(ShoppingCartConstants.COLLECTION, {"user_email": session["email"]})
    items = ShoppingCart.find_items(cart)
    items.remove(request.form["remove"])
    Database.update(ShoppingCartConstants.COLLECTION, {"user_email": session["email"]}, cart.json(cart))
    return render_template("shopping_cart.html")