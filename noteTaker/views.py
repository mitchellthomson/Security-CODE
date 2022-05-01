from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user = current_user)

@views.route('/notes')
def notes():
    return render_template("notes.html", user = current_user)

@views.route('/weather')
def weather():
    return render_template("weather.html", user = current_user)