from flask import Flask
from instance.config import app_config
from app.api.version2 import ver2 as v2


def creat_app(config_name):
    """This method creats app with configuration in the instance folder"""

    app = Flask(__name__, instance_relative_config=True)
    """using instance_relative_config will load config file from instance folder when app created"""
    app.register_blueprint(v2)
    """Registering bluprint to the app"""

    app.config.from_object(app_config['development'])
    """We are loading the default configuration"""

    app.config.from_pyfile('config.py')
    """Loading the configurations from config.py contained in the instance folder"""

    return app
