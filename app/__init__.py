from flask import Flask
from instance.config import app_config


def creat_app(config_name):
    """This method creats app with configuration in the instance folder"""

    app = Flask(__name__, instance_relative_config=True)
    """using instance_relative_config will load config file from instance folder when app created"""

    app.config.from_object(app_config['config_name'])
    """We are loading the default configuration"""

    app.config.from_pyfile('config.py')
    """Loading the configurations from config.py contained in the instance folder"""

    return app
