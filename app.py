from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required
from models import db, User, Album

app = Flask(__name__)
app.config["SECRET_KEY"] = "frostwave_secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///frostwave.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

with app.app_context():
    db.create_all()
    if not User.query.first():
        admin = User(username="admin", password="1234")
        db.session.add(admin)
        db.session.commit()
    if not Album.query.first():
        demo_album = Album(
            title="Winter Lights",
            year="2024",
            description=(
                "The debut album of the band FrostWave, created in Zhytomyr."
                "The music conveys the atmosphere of winter evenings, "
                "quiet streets and neon lights of the city."
            )
        )
        db.session.add(demo_album)
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

@app.route("/album/<int:album_id>")
def album(album_id):
    return render_template(
        "album.html",
        album=Album.query.get_or_404(album_id)
    )

@app.route("/album/add", methods=["GET", "POST"])
@login_required
def add_album():
    if request.method == "POST":
        album = Album(
            title=request.form["title"],
            year=request.form["year"],
            description=request.form["description"]
        )
        db.session.add(album)
        db.session.commit()
        return redirect(url_for("albums"))
    return render_template("edit_album.html", album=None)

@app.route("/album/edit/<int:album_id>", methods=["GET", "POST"])
@login_required
def edit_album(album_id):
    album = Album.query.get_or_404(album_id)
    if request.method == "POST":
        album.title = request.form["title"]
        album.year = request.form["year"]
        album.description = request.form["description"]
        db.session.commit()
        return redirect(url_for("albums"))
    return render_template("edit_album.html", album=album)

@app.route("/album/delete/<int:album_id>")
@login_required
def delete_album(album_id):
    db.session.delete(Album.query.get_or_404(album_id))
    db.session.commit()
    return redirect(url_for("albums"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form["username"],
            password=request.form["password"]
        ).first()
        if user:
            login_user(user)
            return redirect(url_for("albums"))
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
