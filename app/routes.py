from flask import Flask, render_template, request, redirect, url_for
from app import app

posts = []
datas = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({
                'title': title,
                'content': content
            })
            return redirect(url_for('index'))
    return render_template('blog.html', posts=posts)

@app.route('/anketa/', methods=['GET', 'POST'])
def anketa():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        if name and city and hobby and age:
            datas.append({
                'name': name,
                'city': city,
                'hobby': hobby,
                'age': age
            })
            return redirect(url_for('anketa'))
    return render_template('anketa.html', datas=datas)