from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledb' % quote('Admin@123')

db = SQLAlchemy(app)