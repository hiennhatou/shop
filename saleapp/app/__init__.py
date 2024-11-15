from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledb' % quote('Admin@123')
app.config['PAGE_SIZE'] = 2
app.secret_key = 'ewhq982f2q9hgwf768ugq874gtiuwqiuje'
login = LoginManager(app)

db = SQLAlchemy(app)