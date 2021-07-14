from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user,current_user,login_required
auth = Blueprint('auth', __name__)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))




@auth.route('/login',methods=['POST','GET'])
def login():
    if  request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return render_template('home.html', user = current_user)
            else:
                flash('Wrong password')
        else:
            flash('User not registered')
            
        return render_template('login.html')

@auth.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('email already exists', category='success')
        if len(password) < 2:
            flash('password must be longer than 5 characters', category='error')
        if len(name) < 2:
            flash('name must be longer than 1 letter', category='error')
        else:
            new_user = User(name=name, email=email, password= generate_password_hash( password, method='sha256') )
            db.session.add(new_user)
            db.session.commit()
            login_user(user)
            flash('account created!', category='success')
            return redirect(url_for('auth.login'))
        return render_template('signup.html')