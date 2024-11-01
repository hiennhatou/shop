from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app import db, app


class Category(db.Model):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    products = relationship('Product', uselist=True, lazy=True)


class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    description = Column(String(250))
    image = Column(String(250))
    price = Column(Float)
    category_id = Column(Integer, ForeignKey(Category.id))

# if __name__ == "__main__":
#     with app.app_context():
        # db.create_all()
        # db.session.bulk_save_objects(
        #     [Category(name="Mobile"),
        #     Category(name="Tablet"),
        #     Category(name="Laptop")] +
        #     [Product(**p) for p in products]
        # )
        # db.session.commit()
