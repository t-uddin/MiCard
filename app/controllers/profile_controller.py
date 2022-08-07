from flask import Blueprint, render_template, request, redirect
from models.profile import Profile

profile_bp = Blueprint('profile_bp', __name__)


@profile_bp.route('/profile-save', methods=['POST'])
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
def get_profile():
    try:
        userid = "62e6ffd3d1d8472cf1002c4a"
        profile = Profile.get(userid)
        # store(profile)

        sp_list = profile["specialisms"]
        print("Hi", sp_list)
        # print(type(profile.specialisms))



        return render_template('profile.html', profile=profile)

    except Exception as e:
        return ("Error: ", e)


@profile_bp.route('/profile-edit/', methods=['GET', 'POST'])
def get_edit_profile():
    userid = "62e6ffd3d1d8472cf1002c4a"

    if request.method == "POST":
        # # Ensure username was submitted
        # if not request.form.get("username"):
        #     return apology("must provide username", 403)
        #
        # # Ensure password was submitted
        # elif not request.form.get("password"):
        #     return apology("must provide password", 403)
        #
        # # Ensure password and confirm password matches
        # elif request.form.get("password") != request.form.get("password2"):
        #     return apology("passwords do not match", 403)
        #
        # # Query database to ensure username does not already exist
        # rows = db.execute("SELECT * FROM users WHERE username = :username",
        #                   username=request.form.get("username"))
        #
        # if len(rows) != 0:
        #     return apology("username already exists", 403)
        #
        # db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)",
        #             username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))
        #
        # # Redirect user to home page

        # if request.method == "POST":

        # Get updated details
        #     new_bio = request.form.get("new_bio")
        #     new_email = request.form.get("new_email")
        #     new_title = request.form.get("new_title")
        #     new_phone = request.form.get("new_phone")
        #     new_hours = request.form.get("new_hours")
        #     new_location = request.form.get("new_location")
        #     new_field = request.form.get("new_field")
        #     new_registration = request.form.get("new_registration")
        #     new_years = request.form.get("new_years")
        #     new_fee = request.form.get("new_fee")
        #     new_specialisms = request.form.get("new_specialisms")
        #     new_treatments = request.form.get("new_treatments")
        #     new_certifications = request.form.get("new_certifications")
        #     new_education = request.form.get("new_education")
        #     new_interests = request.form.get("new_interests")


        # Create profile object with new details
        updated_profile = Profile(
            id="62e6ffd3d1d8472cf1002c4a",
            bio=request.form.get("new_bio"),
            work_email=request.form.get("new_email"),
            job_title=request.form.get("new_title"),
            phone=request.form.get("new_phone"),
            working_hours=request.form.get("new_hours"),
            location=request.form.get("new_location"),
            field=request.form.get("new_field"),
            registration=request.form.get("new_registration"),
            years_experience=request.form.get("new_years"),
            consultation_fee=request.form.get("new_fee"),
            specialisms=request.form.getlist("new_specialisms"),
            treatments=request.form.getlist("new_treatments"),
            certifications=request.form.getlist("new_certifications"),
            education=request.form.getlist("new_education"),
            interests=request.form.getlist("new_interests"),
            account="62e6f4e8d1d8472cf1002c40")

        # remove empty list items
        updated_profile['specialisms'] = list(filter(len, updated_profile['specialisms']))
        updated_profile['treatments'] = list(filter(len, updated_profile['treatments']))
        updated_profile['certifications'] = list(filter(len, updated_profile['certifications']))
        updated_profile['education'] = list(filter(len, updated_profile['education']))
        updated_profile['interests'] = list(filter(len, updated_profile['interests']))

        # update db
        updated_profile.save()

        # redirect to profile page
        return redirect("/profile")

    else:
        userid = "62e6ffd3d1d8472cf1002c4a"
        profile = Profile.get(userid)

        return render_template("edit_profile.html", profile=profile)
