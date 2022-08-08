from flask import Blueprint, render_template, request, redirect
from models.profile import Profile
from flask_login import login_required, current_user

profile_bp = Blueprint('profile_bp', __name__)


@profile_bp.route('/profile-save', methods=['POST'])
@login_required
def add_profile():
    try:
        profile = Profile(
            work_email="test@hotmail.com",
            job_title="test",
            phone="test",
            field="test",
            specialisms=["test", "test", "test", "test"],
            certifications=["test", "test"],
            education=["test"],
            working_hours="test",
            location="test",
            bio="test",
            registration="test",
            interests=["test", "test"],
            years_experience=13,
            consultation_fee="0",
            voice="Male")
        profile.save()
        # store(profile)
        return
    except Exception as e:
        return ("Error: ", e)


@profile_bp.route('/profile/', methods=['GET'])
@login_required
def get_profile():
    try:
        accountid = current_user.id
        profile = Profile.get(accountid)

        return render_template('profile.html', profile=profile)

    except Exception as e:
        return ("Error: ", e)


@profile_bp.route('/profile-edit/', methods=['GET', 'POST'])
@login_required
def get_edit_profile():
    accountid = current_user.id

    if request.method == "POST":
        # Get user
        user = Profile.objects(account=accountid).first()

        bio = request.form.get("new_bio")
        work_email = request.form.get("new_email")
        job_title = request.form.get("new_title")
        phone = request.form.get("new_phone")
        working_hours = request.form.get("new_hours")
        location = request.form.get("new_location")
        field = request.form.get("new_field")
        registration = request.form.get("new_registration")
        years_experience = request.form.get("new_years")
        consultation_fee = request.form.get("new_fee")
        specialisms = request.form.getlist("new_specialisms")
        treatments = request.form.getlist("new_treatments")
        certifications = request.form.getlist("new_certifications")
        education = request.form.getlist("new_education")
        interests = request.form.getlist("new_interests")

        # remove empty list items
        specialisms = list(filter(len, specialisms))
        treatments = list(filter(len, treatments))
        certifications = list(filter(len, certifications))
        education = list(filter(len, education))
        interests = list(filter(len, interests))

        # update user
        user.update(
            bio=bio,
            work_email=work_email,
            job_title=job_title,
            phone=phone,
            working_hours=working_hours,
            location=location,
            field=field,
            registration=registration,
            years_experience=years_experience,
            consultation_fee=consultation_fee,
            specialisms=specialisms,
            treatments=treatments,
            certifications=certifications,
            education=education,
            interests=interests
        )

        # redirect to profile page
        return redirect("/profile")

    else:
        profile = Profile.get(accountid)
        return render_template("edit_profile.html", profile=profile)
