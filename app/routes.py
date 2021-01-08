from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForms

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mohamed'} # dummy object
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ] # dummy object

    # return render_template('index.html', user=user) - use this to test whether if conditions work in template engine
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)