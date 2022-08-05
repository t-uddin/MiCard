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
    meta = {"collection": "accounts"}

    def to_dict(self):
        return {
                "id": str(self.id),
                "email": self.email,
                "password_hash": self.password_hash,
                "forename": self.forename,
                "surname": self.surname
            }


    def users_index(self):
        # users = User.get()
        # return jsonify({'data': users})
        return "debug"

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