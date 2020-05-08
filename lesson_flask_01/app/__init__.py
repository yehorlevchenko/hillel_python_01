from flask import Flask
from config import Config
from .db import Database

app = Flask(__name__)
app.config.from_object(Config)
app.db = Database()

from app import routes
