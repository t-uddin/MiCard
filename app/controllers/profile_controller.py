from flask import Blueprint, render_template, request, redirect, url_for
from models.profile import Profile
from flask_login import login_required, current_user
from forms import CreateProfileForm
from qrcode import QRCode

profile_bp = Blueprint('profile_bp', __name__)


@profile_bp.route('/profile/', methods=['GET'])
@login_required
def get_profile():
    try:
        account_id = current_user.id
        profile = Profile.get(account_id)
        return render_template('profile.html', profile=profile)

    except Exception as e:
        return "Error: ", e


@profile_bp.route('/avatar/', methods=['GET'])
@login_required
def get_avatar():
    try:
        account_id = current_user.id
        profile = Profile.get(account_id)
        return render_template('avatar.html', profile=profile)

    except Exception as e:
        return "Error: ", e


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
                specialisms=specialisms,
                treatments=treatments,
                certifications=certifications,
                education=education,
                interests=interests
            )

            # update user
            profile.save()

            # redirect to create avatar page
            return redirect(url_for('main.render_create_avatar'))

        else:
            return redirect(url_for("main.render_register_profile"))

    else:
        return render_template(url_for('main.render_register_profile'), form=form)


@profile_bp.route('/avatar-create/', methods=['GET', 'POST'])
@login_required
def create_avatar():
    account_id = current_user.id

    if request.method == "POST":
        # Get user
        user = Profile.objects(account=account_id).first()

        avatar = request.form.get("avatar")
        voice = request.form.get("voice")

        # update profile with avatar details
        user.update(
            avatar_id=avatar,
            voice=voice
        )

        # redirect to profile page
        return redirect("/qr")

    else:
        return render_template("create_avatar.html")


@profile_bp.route('/qr/', methods=['GET'])
@login_required
def create_qr():
    account_id = str(current_user.id)
    host = "https://micard.rzseqhyikaq.eu-gb.codeengine.appdomain.cloud/"

    # Link for users AR page
    input_data = host + "ar2/" + account_id

    # Creating an instance of qrcode
    qr = QRCode(
        version=1,
        box_size=6,
        border=5)

    qr.add_data(input_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save("static/img/qr/" + account_id + '.png')

    return render_template("download-qr.html")
