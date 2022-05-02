from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Note
from . import db
views = Blueprint("views", __name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html", user = current_user)

@views.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "POST":
        note=request.form.get("note")
        new_note = Note(data=note, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
    return render_template("notes.html", user = current_user)

@views.route("/weather")
def weather():
    return render_template("weather.html", user = current_user)