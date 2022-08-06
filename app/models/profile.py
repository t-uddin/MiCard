from mongoengine import (
    Document,
    EmailField,
    IntField,
    ListField,
    StringField,
    ReferenceField,
    BooleanField
)
from .account import Account

class Profile(Document):
    account = ReferenceField("Account", required=True)
    work_email = EmailField(required=True)
    job_title = StringField(required=True)
    phone = StringField(required=True)
    field = StringField(required=True)
    specialisms = ListField(required=True)
    certifications = ListField(required=True)
    education = ListField(required=True)
    working_hours = StringField(required=True)
    location = StringField(required=True)
    bio = StringField(required=True)
    interests = ListField(required=True)
    years_experience = IntField(required=True)
    consultation_fee = StringField(required=False)
    treatments = ListField(required=False)
    registration = StringField(required=False)
    voice = StringField(required=True)
    meta = {"collection": "profiles"}


    def to_dict(self):
        return {
                "id": str(self.id),
                "contact_email": self.work_email,
                "job_title": self.job_title,
                "phone": self.phone,
                "field": self.field,
                "specialisms": self.specialisms,
                "certifications": self.certifications,
                "education": self.education,
                "working_hours": self.working_hours,
                "location": self.location,
                "bio": self.bio,
                "interests": self.interests,
                "exp_years": self.years_experience,
                "cons_fee": self.consultation_fee,
                "treatments": self.treatments,
                "registration": self.registration,
                "voice": self.voice
            }

    @classmethod
    def get(cls, userid):
        ''' Takes user ID and gets details from db '''
        try:
            profile = Profile.objects(id=userid).first().to_dict()
            return profile

        except Exception as e:
            return e

        # return Profile.objects().first().to_dict()

    def store(new_profile):
        ''' Takes a Profile object and saves to db '''
        try:
            new_profile.save()
            return "Success"
        except Exception as e:
            return e



    # def update(userId):
    #     ...

    # def delete(userId):
    #     ...