from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'SOmit' }
    posts = [ # fake array of posts
        { 
            'author': { 'nickname': 'zoom' }, 
            'body': 'Cool' 
        },
        { 
            'author': { 'nickname': 'tim' }, 
            'body': 'The code was so cool!' 
       }
             ]
    return render_template("index.html",
        title = 'HomePage',
        user = user,
        posts=posts)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for openid="'+ form.openid.data + '", remember_me=' + str(form.remember_me.data
            ))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form)