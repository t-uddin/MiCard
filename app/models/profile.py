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
    voice = StringField()
    avatar_id = StringField()
    meta = {"collection": "profiles"}


    def to_dict(self):
        # convert mongoengine lists to python lists
        self.specialisms_list = list.copy(self.specialisms)
        self.certifications_list = list.copy(self.certifications)
        self.education_list = list.copy(self.education)
        self.interests_list = list.copy(self.interests)
        self.treatments_list = list.copy(self.treatments)

        return {
                "id": str(self.id),
                "contact_email": self.work_email,
                "job_title": self.job_title,
                "phone": self.phone,
                "field": self.field,
                "specialisms": self.specialisms_list,
                "certifications": self.certifications_list,
                "education": self.education_list,
                "working_hours": self.working_hours,
                "location": self.location,
                "bio": self.bio,
                "interests": self.interests_list,
                "exp_years": self.years_experience,
                "cons_fee": self.consultation_fee,
                "treatments": self.treatments_list,
                "registration": self.registration,
                "voice": self.voice,
                "avatar_id": self.avatar_id
            }

    @classmethod
    def get(cls, account_id):
        ''' Takes user ID and gets details from db '''
        try:
            profile = Profile.objects(account=account_id).first().to_dict()
            return profile

        except Exception as e:
            return e

    @classmethod
    def get_object(cls, account_id):
        ''' Takes user ID and gets details from db '''
        try:
            profile = Profile.objects(account=account_id).first()
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