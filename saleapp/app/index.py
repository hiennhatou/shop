import math
from hashlib import md5

from app import app, login
from flask import render_template, request, redirect
from flask_login import login_user
import dao
from app.models import User


@app.route("/")
def index():
    print(request.args)
    category_id = request.args.get("category_id")
    pageNumber = int(request.args.get("page") if request.args.get("page") is not None else 1)

    categories = dao.load_catogories()
    products = dao.get_products(category_id, pageNumber)
    return render_template("index.html", categories=categories, products=products,
                           pages=math.ceil(dao.count_product(category_id) / app.config["PAGE_SIZE"]))


@app.route("/login", methods=["get", 'post'])
def loginEndpoint():
    if request.method.__eq__("POST"):
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user = User.query.filter(username == User.username,
                                 md5(password.encode()).hexdigest() == User.password).first()
        if user:
            login_user(user)
            return redirect("/")

    return render_template("login.html")


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
