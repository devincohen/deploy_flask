from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.site_user import Site_User

@app.route('/users')
def show():
    users = Site_User.get_all()
    return render_template('users.html', users = users)

@app.route('/users/new')
def new():
    return render_template('new_user.html')

@app.route('/users/<int:x>')
def show_one(x):
    user = Site_User.get_one(x)
    return render_template('show.html', user=user )

@app.route('/users/<int:x>/edit')
def edit(x):
    user = Site_User.get_one(x)
    return render_template('edit.html', user = user)

@app.route('/add_user', methods=["POST"])
def new_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    Site_User.save(data)
    result = Site_User.get_one_new(data)
    return redirect(f'/users/{result.id}')

@app.route('/edit_user', methods=["POST"])
def edit_user():
    Site_User.update(request.form)
    id = request.form['id']
    return redirect(f'/users/{id}')

@app.route('/users/<int:x>/delete')
def delete(x):
    Site_User.delete(x)
    return redirect('/users')