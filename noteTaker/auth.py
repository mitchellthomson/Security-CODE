from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        psw = request.form.get("psw")
    
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.psw, psw):
                flash('Logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash('Incorrect password, try again!', category='error')
        else:
            flash('Email account not found', category='error')
            
        
    return render_template("login.html")



@auth.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        psw = request.form.get("psw")
        pswRepeat = request.form.get("pswRepeat")
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email is already in use', category='error')
        elif len(email) < 4:
            flash('Email must be longer than 4 characters', category='error')
        elif len(psw) < 8:
            flash('Password must be 8 or more characters', category='error')
        elif psw != pswRepeat:
            flash('Your passwords do not match', category='error')
        else:
            new_user = User(email=email, psw=generate_password_hash(psw, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category="success")
            return redirect(url_for("views.home"))
        
    return render_template("signup.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
