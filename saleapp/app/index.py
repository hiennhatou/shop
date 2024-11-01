from app import app
from flask import render_template, request

import dao

@app.route("/")
def index():
    print(request.args)
    category_id = request.args.get("category_id")
    categories = dao.load_catogories()
    products = dao.get_products(category_id)
    return render_template("index.html", categories=categories, products=products)


if __name__ == '__main__':
    app.run(debug=True)