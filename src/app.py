from flask import Flask, render_template, request, session, redirect, url_for, Blueprint
from src.models.Item.ItemConstants import COLLECTION
from src.common.Database import Database
from src.models.User.User import User
# bluePrints for HTML
from src.models.Item.Views import item_blueprint
from src.models.User.Views import user_blueprint
from src.models.ShoppingCart.Views import shopping_cart_blueprint
from src.models.Review.Views import review_blueprint
app = Flask(__name__)
app.secret_key = "123"


@app.before_first_request
def init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(item_blueprint, url_prefix="/items")
app.register_blueprint(shopping_cart_blueprint, url_prefix="/shopping_cart")
app.register_blueprint(review_blueprint, url_prefix="/review")

app.run(debug=True, port=4992)

