from flask import render_template, url_for, redirect, flash
from app import app
from app.forms import PostForm


@app.route('/')
def index():
    raw_posts = app.db.get_posts()
    messages = list(map(map_posts, raw_posts))
    return render_template('index.html', user='Yehor', messages=messages)

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Posting your shit')
        app.db.save_post(raw_post=form.data)
        return redirect(url_for('index'))

    return render_template('post.html', form=form)

@app.route('/topsecret')
def forbidden():
    return redirect(url_for('index'))

@app.route('/api/get_data')
def test_api():
    return {"_id": "my_freaking_id", "data": {"type": "cat", "voice": "meow"}}


def map_posts(raw_post):
    post = {
        "author": raw_post[0],
        "text": raw_post[1],
    }
    return post
