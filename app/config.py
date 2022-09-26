from flask import Flask, current_app, g
from flask_login import LoginManager
import mongoengine
import certifi
from environment import mongo_host, secret_key
from flask_cors import CORS, cross_origin


# connect to db
mongoengine.connect(host=mongo_host, tlsCAFile=certifi.where())

login_manager = LoginManager()


def create_app():
    # initiate app
    app = Flask(__name__)

    # update environment variables
    app.config["SECRET_KEY"] = secret_key
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Allow cross origin requests from AR app
    cors = CORS(app)

    # register blueprints
    register_blueprints(app)

    # initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = "account_bp.login"

    return app


def register_blueprints(app):
    from controllers.profile_controller import profile_bp
    app.register_blueprint(profile_bp)

    from routes.routes import main
    app.register_blueprint(main)

    from controllers.account_controller import account_bp
    app.register_blueprint(account_bp)

    from controllers.chat_controller import chat_bp
    app.register_blueprint(chat_bp)

