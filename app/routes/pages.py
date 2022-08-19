from flask import render_template, redirect, url_for, request, flash, Blueprint
from flask_login import login_required, current_user
from forms import editProfileForm

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('home.html')
    else:
        return render_template('index.html')


@main.route('/home')
@login_required
def home():
    return render_template('home.html')


@main.route('/avatar/')
@login_required
def render_():
    return render_template('login.html')


@main.route('/ar/')
def render_ar():
    return redirect(url_for('static', filename='ar_app/index.html', title="HELLOOO"))


@main.route('/ar2/')
def render_ar2():
    return render_template('ar-iframe.html')
