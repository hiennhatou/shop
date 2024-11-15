from app import app
from app.models import Category, Product


def load_catogories():
    return Category.query.order_by('name').all()


def get_products(category_id, pageNumber):
    query = Product.query.order_by('name')
    if category_id is not None:
        query = query.filter(Product.category_id == category_id)
    start = (pageNumber - 1) * app.config['PAGE_SIZE']
    query = query.slice(start, start + app.config['PAGE_SIZE'])
    return query.all()

def count_product(category_id):
    query = Product.query
    if category_id is not None:
        query = query.filter(Product.category_id == category_id)
    return query.count()
