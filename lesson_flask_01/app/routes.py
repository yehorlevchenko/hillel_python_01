from flask import render_template, url_for, redirect
from app import app


@app.route('/')
def index():
    messages = [
        {"text": "First broadcast",
        "author": "Yehor"},
        {"text": "Beep-boop",
        "author": "Robot"}
    ]
    return render_template('index.html', user='Yehor', messages=messages)

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/topsecret')
def forbidden():
    return redirect(url_for('index'))
