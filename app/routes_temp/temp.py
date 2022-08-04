# from flask import abort, render_template, redirect, url_for
# from markupsafe import escape
# from app import app
#
# @app.route('/')
# def render_home():
#     return render_template('index.html')
#
# @app.route('/login/')
# def render_login():
#     return render_template('login.html')
#
# @app.route('/ar/')
# def render_ar():
#     return redirect(url_for('static', filename='ar_app/ar.html', title="HELLOOO"))
#
# @app.route('/ar2/')
# def render_ar2():
#     return render_template('ar-iframe.html')
#
# # flask examples
# @app.route('/about/')
# def about():
#     return '<h3>This is a Flask web application.</h3>'
#
# @app.route('/capitalize/<word>/')
# def capitalize(word):
#     return '<h1>{}</h1>'.format(escape(word.capitalize()))
#
# @app.route('/add/<int:n1>/<int:n2>/')
# def add(n1, n2):
#     return '<h1>{}</h1>'.format(n1 + n2)
#
# @app.route('/users/<int:user_id>/')
# def greet_user(user_id):
#     users = ['Bob', 'Jane', 'Adam']
#     try:
#         return '<h2>Hi {}</h2>'.format(users[user_id])
#     except IndexError:
#         abort(404)
#
