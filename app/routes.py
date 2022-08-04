# from run import app
from flask import render_template, redirect, url_for, request, flash, Blueprint
import app.controllers.ProfileController as Profile
from forms import editProfileForm

main = Blueprint('main', __name__)

@main.route('/layout')
def render_home():
    return render_template('inherit.html', title="LAYOUT")


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login/')
def render_login():
    return render_template('login.html')


@main.route('/ar/')
def render_ar():
    return redirect(url_for('static', filename='ar_app/ar.html', title="HELLOOO"))


@main.route('/ar2/')
def render_ar2():
    return render_template('ar-iframe.html')


@main.route('/getprofile/')
def profile_get():
    return Profile.index()


# @main.route('/adduser/')
# def users_add():
#     return User.store()


@main.route('/editprofile/', methods=["POST", "GET"])
def edit_profile():
    if request.method == "POST":
        print(db)
        form = editProfileForm(request.form)
        new_forename = form.forename.data
        new_surname = form.surname.data
        new_voice = form.voice.data

        db.users.insert_one({
            "forename": new_forename,
            "surname": new_surname
        })

        flash("Profile successfully updated", "success")
        return redirect("/")
    else:
        form = editProfileForm()
        return render_template('edit_profile.html', form=form)
