from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        surname = request.form['surname']
        salary = request.form['salary']
        phone = request.form['phone']
        cname = request.form['cname']
        new_user = User(email=email, name=name, surname=surname, salary=salary, phone=phone, cname=cname)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_user.html')

@main.route('/update_user/<email>', methods=['GET', 'POST'])
def update_user(email):
    user = User.query.get(email)
    if request.method == 'POST':
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.salary = request.form['salary']
        user.phone = request.form['phone']
        user.cname = request.form['cname']
        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('update_user.html', user=user)

@main.route('/delete_user/<email>')
def delete_user(email):
    user = User.query.get(email)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!')
    return redirect(url_for('main.index'))
