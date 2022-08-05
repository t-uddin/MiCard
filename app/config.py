from flask import Flask, current_app, g
import mongoengine
import certifi
from environment import mongo_host
# from werkzeug.local import LocalProxy
# import bson
# from routes.user_bp import user_bp

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "d18e4f677ec08636a373abcd1234"
# app.config["MONGO_URI"] = "mongodb+srv://mongo:mongo@cluster0.q3gpfnl.mongodb.net/micard?retryWrites=true&w=majority"
#
# # blueprints
# app.register_blueprint(user_bp, url_prefix='/users')
#
# # setup db
# mongodb_client = PyMongo(app, tlsCAFile=certifi.where())
# db = mongodb_client.db
# print(db)
#
# from app import routes
# import app

mongoengine.connect(host=mongo_host, tlsCAFile=certifi.where())

def create_app():
    app = Flask(__name__)
    # app.config["MONGO_URI"] = mongo_host
    app.config["SECRET_KEY"] = "d18e4f677ec08636a373abcd1234"

    register_blueprints(app)

    return app


def register_blueprints(app):
    from routes.profile_bp import profile_bp
    app.register_blueprint(profile_bp)

    from routes.temp import main
    app.register_blueprint(main)
