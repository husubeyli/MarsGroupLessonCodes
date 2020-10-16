from flask import render_template

from run import app


@app.route('/home')
def home_page():
    return 'Salam Eyyub '

@app.route('/aboutme')
def about_me():
    user_name = 'Enver'
    user_surname = 'Ezimov'
    return render_template('my_htmls/aboutme.html', user_name_val=user_name, user_surname=user_surname)