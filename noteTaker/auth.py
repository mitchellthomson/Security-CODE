from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        psw = request.form.get('psw')
        pswRepeat = request.form.get('pswRepeat')
        
        if len(email) < 4:
            flash('Email must be longer than 4 characters', category='error')
        elif len(psw) < 8:
            flash('Password must be 8 or more characters', category='error')
        elif psw != pswRepeat:
            flash('Your passwords do not match', category='error')
        else:
            new_user = User(email=email, psw=generate_password_hash(psw, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash("Account Created!", category='success')
            return redirect(url_for("views.home"))
        
    return render_template("signup.html")

