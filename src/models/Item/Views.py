from flask import Blueprint, request, render_template, session

from src.common.Database import Database
from src.models.Item import ItemConstants
from src.models.Item.Item import Item
from src.models.ShoppingCart import ShoppingCartConstants
from src.models.ShoppingCart.ShoppingCart import ShoppingCart
import src.models.User.decorators as user_decorators
item_blueprint = Blueprint("Item", __name__)


@item_blueprint.route('/create', methods=['GET', 'POST'])
@user_decorators.requires_admin_permission
def create_item():
    if request.method == 'POST':
        title = request.form["title"]
        description = request.form["description"]
        size = request.form["size"]
        category = request.form["category"]
        price = request.form["price"]
        if title == '':
            print("title is none")
        elif description == "":
            print("no colour")
        elif size == "":
            print("no size")
        elif category == "":
            print("no material")
        elif price == '':
            print("no price")
        else:
            item = Item(title, description, size, category, price)
            print(item.json())
            item.save_to_db()
            return render_template('home.html')
    return render_template('create_item_ADMIN.html')


# need to update method to be a more simple way to remove item.
@item_blueprint.route('/remove', methods=['GET', 'POST'])
def remove_item():
    if request.method == 'POST':
        title = request.form["title"]
        colour = request.form["colour"]
        size = request.form["size"]
        if title == '':
            print("title is none")
        elif colour == "":
            print("no colour")
        elif size == "":
            print("no size")
        else:
            Database.remove(ItemConstants.COLLECTION, {"title": title, "colour": colour, "size": size})
            return render_template('home.html')
    return render_template('create_item_ADMIN.html')


# this also needs updating.
@item_blueprint.route('/update', methods=['GET', 'POST'])
def go_to_update_item():
    _id = request.form["Edit"]
    item = Database.find_one(ItemConstants.COLLECTION, {"_id": _id})
    return render_template("edit_item.html", item=item)


@item_blueprint.route('/update_item', methods=['POST'])
def update_item():
    title = request.form["title"]
    description = request.form["description"]
    size = request.form["size"]
    category = request.form["category"]
    price = request.form["price"]
    _id = request.form["_id"]
    item = Item(title, description, size, category, price, _id)
    Database.update(ItemConstants.COLLECTION, {"_id": _id}, item.json())
    return render_template("home.html")


@item_blueprint.route('/view')
def item_view():
    items = Item.all()
    return render_template("item_view.html", items=items)


@item_blueprint.route('/Girls')
def item_view_girls():
    items = Item.all_from_category("1")
    return render_template("item_view_girls.html", items=items)
# title=items['title'], colour=items['colour'], size=items['size'], material=items['material'], price=items['price']


@item_blueprint.route('/Boys')
def item_view_boys():
    items = Item.all_from_category("2")
    return render_template("item_view_boys.html", items=items)


@item_blueprint.route('/Women')
def item_view_women():
    items = Item.all_from_category("3")
    return render_template("item_view_women.html", items=items)


@item_blueprint.route('/Accessories')
def item_view_accessories():
    items = Item.all_from_category("4")
    return render_template("item_view_accessories.html", items=items)


@item_blueprint.route('/Aprons')
def item_view_aprons():
    items = Item.all_from_category("5")
    return render_template("item_view_accessories.html", items=items)


@item_blueprint.route('/item', methods=['POST'])
def buy_item():
    if request.method == 'POST':
        if 'email' not in session.keys():
            cart = ShoppingCart("12:00", True)
            session["email"] = cart.user_email
            cart.add_item(request.form["Buy"])
            cart.save_to_db()
            print("if")
            return render_template("home.html")

        else:
            cart = ShoppingCart.find_by_user_id(session["email"])
            ShoppingCart.add_item(cart, request.form["Buy"])
            Database.update(ShoppingCartConstants.COLLECTION, {"user_email": session["email"]}, cart.json(cart))
            return render_template("home.html")
    else:
        return render_template("home.html")
