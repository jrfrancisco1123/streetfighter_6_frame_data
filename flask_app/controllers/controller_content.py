from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.models_content import Content
from flask_app.models.models_user import User

# Create a post page
@app.route('/create')
def create():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('create.html')

# Update a post
@app.route('/update/post/<int:post_id>')
def update(post_id):
    if 'user_id' not in session:
        return redirect('/')
    current_user = User.get_id({'id': session['user_id']})
    post = Content.get_one({'id': post_id})
    return render_template('update.html', current_user=current_user, post=post)

# Delete a post
@app.route('/delete/post/<int:post_id>')
def delete(post_id):
    if 'user_id' not in session:
        return redirect('/')
    Content.delete({'id': post_id})
    return redirect('/dashboard')

# --------------------- POST ---------------------
# Create post route
@app.post('/process/create')
def post_content():
    if 'user_id' not in session:
        return redirect('/login')
    if not Content.validations(request.form):
        return redirect('/create')
    data = {
        'subject': request.form['subject'],
        'message': request.form['message'],
        'user_id': session['user_id']
    }
    Content.save(data)
    return redirect('/dashboard')

# Update post route
@app.post('/process/update/<int:post_id>')
def update_content(post_id):
    if 'user_id' not in session:
        return redirect('/login')
    if not Content.validations(request.form):
        return redirect(f'/update/post/{post_id}')
    data = {
        'subject': request.form['subject'],
        'message': request.form['message'],
        'user_id': session['user_id'],
        'id': post_id
    }
    Content.update(data)
    return redirect('/dashboard')
