from mongoengine import (
    Document,
    EmailField,
    IntField,
    ListField,
    StringField,
    ReferenceField,
    BooleanField
)
from config import login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash

@login_manager.user_loader
def load_user(user_id):
    """Load the user object from the user ID stored in the session"""
    return Account.objects(pk=user_id).first()


class Account(Document, UserMixin):
    email = StringField(required=True)
    password_hash = StringField(required=True)
    forename = StringField(required=True)
    surname = StringField(required=True)
    meta = {"collection": "accounts"}

    def to_dict(self):
        return {
                "id": str(self.id),
                "email": self.email,
                "password_hash": self.password_hash,
                "forename": self.forename,
                "surname": self.surname
            }

    def check_password(self, password):
        """Checks that the pw provided hashes to the stored pw hash value"""
        return check_password_hash(self.password_hash, password)


    def store(self):
        # dic = {"forename": "Thamanna", "surname": "Uddin"}
        # x = user_collection.insert_one(dic)
        # print(x)
        pass

    def show(userId):
        pass

    def update(userId):
        pass

    def delete(userId):
        pass