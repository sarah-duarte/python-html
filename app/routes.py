from flask import render_template, request, redirect, url_for, flash
from app import app
from flask_login import current_user, login_user, logout_user
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Sarah'}
    posts = [
        { 'author': {'username': 'John'}, 'body': 'Beautiful day in Portland!' },
        { 'author': {'username': 'Susan'}, 'body': 'The Avengers movie was so cool!' },
        { 'author': {'username': 'Miguel'}, 'body': 'The Avengers movie was so cool!' }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == "POST":
        user = User.query.filter_by(username=request.values.get("user")).first()
        if user is None or not user.password == request.values.get("pass"):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        r = request.values.get("remember") == "on"
        login_user(user, remember=r)
        return redirect(url_for('index'))
    return render_template("login.html" , title="Login")