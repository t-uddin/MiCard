from flask import render_template, redirect, url_for, request, flash, Blueprint
from models.account import Account
from forms import editProfileForm

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


