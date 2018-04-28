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
            total = 0
            for item in items:
                total += float(item["price"])
            return render_template("shopping_cart.html", items=items, total=total)
        return render_template("shopping_cart.html")


@shopping_cart_blueprint.route("/cart", methods=['GET', 'POST'])
def empty_cart():
    return render_template("shopping_cart.html")


@shopping_cart_blueprint.route("/remove", methods=['POST'])
def remove_item():
    cart = ShoppingCart.find_by_user_id(session["email"])
    cart_ids = cart.shopping_list
    cart_ids.remove(request.form["remove"])
    Database.update(ShoppingCartConstants.COLLECTION, {"user_email": session["email"]}, cart.json(cart))
    items = ShoppingCart.find_items(cart.json(cart))
    total = 0
    for item in items:
        total += float(item["price"])
    return render_template("shopping_cart.html", items=items, total=total)
