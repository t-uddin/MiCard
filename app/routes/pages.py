from flask import render_template, redirect, url_for, request, flash, Blueprint
from forms import editProfileForm

main = Blueprint('main', __name__)

@main.route('/layout')
def render_home():
    return render_template('inherit.html', title="")


@main.route('/')
def index():
    # TODO: if logged in send to home else send to index
    return render_template('index.html')

@main.route('/home')
def home():
    # TODO: if logged in send to home else send to index
    return render_template('home.html')


# @main.route('/login/')
# def render_login():
#     return render_template('login.html')


@main.route('/ar/')
def render_ar():
    return redirect(url_for('static', filename='ar_app/ar.html', title="HELLOOO"))


@main.route('/ar2/')
def render_ar2():
    return render_template('ar-iframe.html')



# @main.route('/inherit/')
# def render_nnjar2():
#     return render_template('inherit.html')


# @main.route('/getprofile/')
# def profile_get():
#     return Profile.index()


