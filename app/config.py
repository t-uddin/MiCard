from flask import Flask, current_app, g
from flask_login import LoginManager
import mongoengine
import certifi
from environment import mongo_host, secret_key
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


# connect to db
mongoengine.connect(host=mongo_host, tlsCAFile=certifi.where())

login_manager = LoginManager()


def create_app():
    # initiate app
    app = Flask(__name__)

    # update environment variables
    app.config["SECRET_KEY"] = secret_key

    # register blueprints
    register_blueprints(app)

    # initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = "users.login"

    return app


def register_blueprints(app):
    from controllers.profile_controller import profile_bp
    app.register_blueprint(profile_bp)

    from routes.pages import main
    app.register_blueprint(main)

    from controllers.account_controller import account_bp
    app.register_blueprint(account_bp)

