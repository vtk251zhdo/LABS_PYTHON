from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from models import db, User, Album


app = Flask(__name__)
app.config['SECRET_KEY'] = 'NewYear2026Secret!'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frostwave.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()
    if not User.query.first():
        admin = User(username="admin", password="1234")
        db.session.add(admin)
        db.session.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/albums")
def albums():
    return render_template("albums.html", albums=Album.query.all())
