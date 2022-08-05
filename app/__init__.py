# from flask import Flask, current_app, g
# from flask_pymongo import PyMongo
# import certifi
#
# def create_app():
#     app = Flask(__name__)
#     app.config["MONGO_URI"] = "mongodb+srv://mongo:mongo@cluster0.q3gpfnl.mongodb.net/micard?retryWrites=true&w=majority"
#     app.config["SECRET_KEY"] = "d18e4f677ec08636a373abcd1234"
#
#     # setup db
#     mongodb_client = PyMongo(app, tlsCAFile=certifi.where())
#     db = mongodb_client.db
#
#     register_blueprints(app)
#     register_extensions(app)
#
#     return app
#
#
# def register_blueprints(app):
#     from routes.user_bp import user_bp
#     app.register_blueprints(user_bp)
#
#
# def register_extensions(app):
#     pass