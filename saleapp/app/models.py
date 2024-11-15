from hashlib import md5

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum as DBEnum
from sqlalchemy.orm import relationship
from enum import Enum as SystemEnum
from flask_login import UserMixin

from app import db, app


class UserEnum(SystemEnum):
    ADMIN = 'admin'
    USER = 'user'


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


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userRole = Column(DBEnum(UserEnum))
    name = Column(String(250))
    username = Column(String(250), unique=True)
    password = Column(String(300))


products = [{
    "name": "iPhone 7 Plus",
    "description": "Apple, 32GB, RAM: 3GB, iOS13",
    "price": 17000000,
    "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg",
    "category_id": 1
}, {
    "name": "iPad Pro 2020",
    "description": "Apple, 128GB, RAM: 6GB",
    "price": 37000000,
    "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
    "category_id": 2
}, {
    "name": "iPad Pro 2021",
    "description": "Apple, 128GB, RAM: 6GB",
    "price": 37000000,
    "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
    "category_id": 2
}, {
    "name": "iPad Pro 2022",
    "description": "Apple, 128GB, RAM: 6GB",
    "price": 37000000,
    "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
    "category_id": 2
}, {
    "name": "iPad Pro 2023",
    "description": "Apple, 128GB, RAM: 6GB",
    "price": 37000000,
    "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
    "category_id": 2
}, {
    "name": "iPad Pro 2024",
    "description": "Apple, 128GB, RAM: 6GB",
    "price": 37000000,
    "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1690528735/cg6clgelp8zjwlehqsst.jpg",
    "category_id": 2
}]

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        user = User()
        user.username = 'hiennhatt'
        user.userRole = UserEnum.ADMIN
        user.password = md5("Admin@123".encode(encoding="utf-8")).hexdigest()
        user.name = "Hien Nguyen"
        db.session.add(user)
        db.session.commit()
        db.session.bulk_save_objects(
            [Category(name="Mobile"),
             Category(name="Tablet"),
             Category(name="Laptop")] +
            [Product(**p) for p in products]
        )
        db.session.commit()
