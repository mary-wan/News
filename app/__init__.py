from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap   #initialise boostrap
from config import config_options
from app import views
from app import error
from app import app 

bootstrap = Bootstrap()

def create_app(config_name):


    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

   # Initializing flask extensions
    bootstrap.init_app(app)

    return app

def create_app(config_name):
    #....
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app


    from app import views
    from app import error

    return app

