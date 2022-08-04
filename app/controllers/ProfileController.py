# pseudo code
import sys
from flask import render_template, redirect, url_for, request, abort
from models.profile import Profile
# from run import db
# user_collection = db.users
from models.profile import Profile




def index():
    print(Profile.objects().first())
    return Profile.objects().first().to_dict()

# def store():
#     dic = {"forename": "Thamanna", "surname": "Uddin"}
#     x = user_collection.insert_one(dic)
#     print(x)
#     return "Hi"
#
# def show():
#     query = { "forename": "John" }
#     user = user_collection.find(query)
#     return user
#
# def update(userId):
#     ...
# def delete(userId):
#     ...