from app.models import Category, Product


def load_catogories():
    return Category.query.order_by('name').all()


def get_products(category_id):
    query = Product.query.order_by('name')
    if category_id is not None:
        query = query.filter(Product.category_id == category_id)
    return query.all()
