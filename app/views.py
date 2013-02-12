from flask import render_template
from app import app

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