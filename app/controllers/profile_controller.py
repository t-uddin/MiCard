from flask import Blueprint, render_template, request, redirect, url_for
from models.profile import Profile
from flask_login import login_required, current_user
from forms import CreateProfileForm


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
        account_id = current_user.id
        profile = Profile.get(account_id)
        return render_template('profile.html', profile=profile)

    except Exception as e:
        return ("Error: ", e)


def get_raw(account_id):
    profile = Profile.get_object(account_id)
    return profile


def to_dict(profile):
    profile = profile.to_dict()
    return profile


@profile_bp.route('/profile-edit/', methods=['GET', 'POST'])
@login_required
def get_edit_profile():
    account_id = current_user.id

    if request.method == "POST":
        # Get user
        user = Profile.objects(account=account_id).first()

        bio = (request.form.get("new_bio")).strip()
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
        profile = Profile.get(account_id)
        return render_template("edit_profile.html", profile=profile)



@profile_bp.route('/profile-create/', methods=['GET', 'POST'])
@login_required
def get_create_profile():
    account_id = current_user.id

    if request.method == "POST":
        # get form data
        bio = (request.form.get("new_bio")).strip()
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

        # create and save profile object

        profile = Profile(
            account=account_id,
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

        print(profile)
        # update user
        profile.save()

        # redirect to profile page
        return redirect("/profile")

    else:
        return redirect(url_for('main.render_create_avatar'))


@profile_bp.route('/profile-register/', methods=['GET', 'POST'])
@login_required
def get_register_profile():
    account_id = current_user.id
    form = CreateProfileForm()

    if request.method == "POST":

        if form.validate_on_submit():
            # gather form list data
            specialisms = request.form.getlist("specialisms")
            treatments = request.form.getlist("treatments")
            certifications = request.form.getlist("certifications")
            education = request.form.getlist("education")
            interests = request.form.getlist("interests")

            # remove empty list items
            specialisms = list(filter(len, specialisms))
            treatments = list(filter(len, treatments))
            certifications = list(filter(len, certifications))
            education = list(filter(len, education))
            interests = list(filter(len, interests))

            print(specialisms)

            # save form data to a new profile object
            profile = Profile(
                account=account_id,
                bio=form.bio.data.strip(),
                work_email=form.email.data,
                job_title=form.job.data,
                phone=form.phone.data,
                working_hours=form.hours.data,
                location=form.location.data,
                field=form.field.data,
                registration=form.registration.data,
                years_experience=form.years.data,
                consultation_fee=str(form.fee.data),
                # specialisms=form.specialisms.data,
                specialisms=specialisms,
                treatments=treatments,
                certifications=certifications,
                education=education,
                interests=interests
            )

            print(profile)
            # update user
            profile.save()

            # redirect to create avatar page
            return redirect(url_for('main.render_create_avatar'))

        else:
            print("error in form")

    else:
        return render_template(url_for('main.render_register_profile'), form=form)


