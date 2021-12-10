from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# app.wsgi_app = ProxyFix(app.wsgi_app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:fatec@localhost:3306/calculadoradb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)