from flask import render_template, redirect, url_for, request, flash, Blueprint
from flask_login import login_required, current_user
from forms import editProfileForm, CreateProfileForm

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


@main.route('/create-profile')
@login_required
def render_create_profile():
    return render_template('create_profile.html')


@main.route('/profile-register')
@login_required
def render_register_profile():
    return render_template('register_profile.html', form=CreateProfileForm())


@main.route('/create-avatar')
@login_required
def render_create_avatar():
    return render_template('create_avatar.html')


@main.route('/ar/')
def render_ar():
    return redirect(url_for('static', filename='ar_app/index.html', title="HELLOOO"))

@main.route('/ar2/')
def render_ar2():
    return redirect(url_for('static', filename='ar_app2/index.html'))


@main.route('/ar-frame/')
def render_ar_iframe():
    return render_template('ar-iframe.html')
