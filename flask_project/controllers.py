from flask import render_template, request
from run import app
from models import User

@app.route('/')
def user_list_page():
    users = User.query.all()
    print(users)
    return render_template('user_list.html', user_list = users)


@app.route('/create', methods=['POST',])
def create_user():
    print('Melumatlar gonderildi')
    print(request.form)

    user = User(username=request.form['username'], email=request.form['email'], full_name=request.form['full_name'])

    user.save()

    users = User.query.all()
    print(users)
    return render_template('user_list.html', user_list = users)
