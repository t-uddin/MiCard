from models.profile import Profile

def get(profile):
    # return Profile.objects().first().to_dict()

    pass


def store(new_profile):
    ''' Takes a Profile object and saves to db '''
    try:
        new_profile.save()
        return "Success"
    except Exception as e:
        return e


# def show():
#     query = { "forename": "John" }
#     user = user_collection.find(query)
#     return user
#
# def update(userId):
#     ...
# def delete(userId):
#     ...