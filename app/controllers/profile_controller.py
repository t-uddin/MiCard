from flask import Blueprint
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
            interests=["test", "test"],
            years_experience=13,
            consultation_fee="0",
            voice="Male")
        profile.save()
        # store(profile)
        return
    except Exception as e:
        return ("Error: ", e)


@profile_bp.route('profile-get', methods=['GET'])
def get_profile():
    try:
        Profile.get(1234)
        return
    except Exception as e:
        return ("Error: ", e)

