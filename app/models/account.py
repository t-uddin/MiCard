from mongoengine import (
    Document,
    EmailField,
    IntField,
    ListField,
    StringField,
    ReferenceField,
    BooleanField
)

class Account(Document):
    email = StringField(required=True)
    password_hash = StringField(required=True)
    forename = StringField(required=True)
    surname = StringField(required=True)
    meta = {"collection": "profiles"}

    def to_dict(self):
        return {
                "id": str(self.id),
                "email": self.email,
                "password_hash": self.password_hash,
                "forename": self.forename,
                "surname": self.surname
            }
