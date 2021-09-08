"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, flash
from models import Cupcake, connect_db, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "secret123"

connect_db(app)