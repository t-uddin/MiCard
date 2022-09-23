from flask import render_template, redirect, request, flash, Blueprint, url_for
from models.account import Account
from forms import editProfileForm, RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, login_required


account_bp = Blueprint('account_bp', __name__)

# @account_bp.route('/editaccount/', methods=["POST", "GET"])
# @login_required
# def edit_account():
#     if request.method == "POST":
#         userid ="TODO"
#         form = editProfileForm(request.form)
#         new_forename = form.forename.data
#         new_surname = form.surname.data
#         email = "test"
#         password_hash = "test"
#
#         account = Account(id=userid, forename=new_forename, surname=new_surname, email=email, password_hash=password_hash)
#         account.save()
#
#         flash("Profile successfully updated", "success")
#         return redirect("/")
#
#     else:
#         form = editProfileForm()
#         return render_template('edit_profile.html', form=form)
#     pass


@account_bp.route('/register/', methods=["GET", "POST"])
def register():
    """Registers the user with username, email and password hash in database"""

    logout_user()
    form = RegistrationForm()
    # form.validate_on_submit()

    if request.method == "POST":
        # Ensure password and confirm password matches
        if form.password.data != form.confirm_psw.data:
            flash("Passwords do not match.", category="warning")
            return redirect(url_for("account_bp.register"))

        # Ensure email is not already registered
        elif Account.get(form.email.data) is not None:
            flash("An account already exists with this email", category="warning")
            return redirect(url_for("account_bp.register"))

        elif form.validate_on_submit():
            password_hash = generate_password_hash(form.password.data)
            account = Account(
                email=form.email.data,
                forename=form.forename.data,
                surname=form.surname.data,
                password_hash=password_hash,
            )
            account.save()

            flash("Thanks for registering!", category="success")

            login_user(account)
            return redirect(url_for('main.render_register_profile'))

        else:
            flash("An error occurred", category="warning")
            return redirect(url_for("account_bp.register"))

    else:
        return render_template('register_account.html', form=form)


@account_bp.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    """Logs the user in through username/password"""
    if request.method == "POST":
        logout_user()
        if form.validate_on_submit():
            # Grab the user from a user model lookup
            email = form.email.data
            account = Account.objects(email=email).first()

            # Ensure user exists and password is correct
            if account is not None and account.check_password(form.password.data):
                login_user(account)
                return redirect(url_for("main.home"))

            else:
                flash("There is no account with this email/password combination.", category="danger")

        return render_template("login.html", form=form)

    else:
        return render_template("login.html", form=form)


@account_bp.route("/logout/")
@login_required
def logout():
    """Log out the current user"""
    logout_user()
    flash("You have logged out.", category="success")
    return redirect("/")
