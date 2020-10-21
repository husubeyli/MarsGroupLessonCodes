from flask import render_template, request, redirect, flash
from run import app
from models import User

from forms import UserForm

@app.route('/')
def user_list_page():
    users = User.query.all()
    return render_template('user_list.html', user_list = users)


@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(username=request.form['username'], email=request.form['email'], full_name=request.form['full_name'])
            user.save()
            flash('User yaradildi')
            return redirect('/')
        else:
            flash('Sehvlik var')
    return render_template('create_user.html', form=form)
