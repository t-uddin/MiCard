from flask import render_template, redirect, url_for, request, flash, Blueprint
from models.account import Account
from forms import editProfileForm, RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, login_required



account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/editaccount/', methods=["POST", "GET"])
def edit_account():
    if request.method == "POST":
        form = editProfileForm(request.form)
        new_forename = form.forename.data
        new_surname = form.surname.data
        new_voice = form.voice.data
        email ="test@email.com"
        password_hash = "test"

        account = Account(forename=new_forename, surname=new_surname, email=email, password_hash=password_hash)
        account.save()

        flash("Profile successfully updated", "success")
        return redirect("/")

    else:
        form = editProfileForm()
        return render_template('edit_profile.html', form=form)
    pass


@account_bp.route('/register/', methods=["GET", "POST"])
def register():
    """Registers the user with username, email and password hash in database"""
    form = RegistrationForm()

    if request.method == "POST":
        print("1")
        logout_user()
        print("2")
        if form.validate_on_submit():
            print("3")
            password_hash = generate_password_hash(form.password.data)
            print("4", password_hash)
            account = Account(
                email=form.email.data,
                forename=form.forename.data,
                surname=form.surname.data,
                password_hash=password_hash,
            )
            print("5", account)
            account.save()
            print("success")
            flash("Thanks for registering!", category="success")
            return login_and_redirect(account)
        else:
            return "Error Occurred."

    else:
        return render_template('register_account.html', form=form)


def login_and_redirect(account):
    """Logs in user, flashes welcome message and redirects to index"""
    login_user(account)
    flash(f"Welcome {account.forename}!", category="success")
    return redirect("../profile")


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

            if account is not None and account.check_password(form.password.data):
                # User validates (user object found and password for that
                # user matched the password provided by the user)
                return login_and_redirect(account)
            else:
                flash(
                    "(email or username)/password combination not found", category="error"
                )

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

