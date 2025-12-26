from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from models import db, User, Album


app = Flask(__name__)
app.config['SECRET_KEY'] = 'NewYear2026Secret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frostwave.db'

db.init_app(app)

