from flask import Flask

app = Flask(__name__)

# app is the directory and views is the file
from app import views
from app import admin_views