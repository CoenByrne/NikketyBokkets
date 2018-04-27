from flask import Blueprint, request, session, render_template

from src.models.ShoppingCart.ShoppingCart import ShoppingCart
from src.models.User.User import User

user_blueprint = Blueprint("User", __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.register_user(email, password):
            session['email'] = email
            cart = ShoppingCart("00:00", False, email)
            cart.save_to_db()
            return render_template("home.html")
    return render_template("register.html")


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.login_user(email, password):
            session['email'] = email
            return render_template("home.html")
        else:
            print("Wrong password")
    return render_template("login.html")

