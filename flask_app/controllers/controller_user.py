from flask_app import app
from flask import render_template, request, redirect, session, flash

from flask_app.models.models_user import User
from flask_app.models.models_content import Content

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Default page
@app.route('/')
def index():
    return render_template('index.html')

# Login page
@app.route('/login')
def login_page():
    return render_template('login.html')

# Registration page
@app.route('/register')
def registration_page():
    return render_template('registration.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    current_user = User.get_id({'id': session['user_id']})
    all_posts = Content.content_with_users()
    return render_template('dashboard.html', current_user=current_user, all_posts=all_posts)

# Logout
@app.route('/signout')
def signout():
    session.clear()
    return redirect('/login')

# --------------------- POST ---------------------

# Register new user post route
@app.post('/process/register')
def register_user():
    if not User.validations(request.form):
        return redirect('/register')
    data = {
        'email': request.form['email'],
        'username': request.form['username'],
        'password': bcrypt.generate_password_hash(request.form['password']),
        'confirm_password': request.form['confirm_password']
    }
    user = User.save(data)
    session['user_id'] = user
    return redirect('/dashboard')

# Login a user post route
@app.post('/process/login')
def login_user():
    registered_user = User.get_email({'email': request.form['email']})
    if not registered_user:
        flash("Invalid/Email Password", 'login')
        return redirect('/login')
    if not bcrypt.check_password_hash(registered_user.password, request.form['password']):
        flash("Invalid/Email Password", 'login')
        return redirect('/login')
    session['user_id'] = registered_user.id
    return redirect('/dashboard')