from flask import Flask
# from pgmanagedconnection import ManagedConnection
from instance.config import app_config
from app.db_con import DataBaseConnection
from app.api.version2 import ver2 as v2


def creat_app(config_name):
    """This method creats app with configuration in the instance folder"""
    # We will be using the config variable to determine the database

    app = Flask(__name__, instance_relative_config=True)
    """using instance_relative_config will load config file from instance folder when app created"""
    """Loading the configurations from config.py contained in the instance folder"""
    app.register_blueprint(v2)
    """Registering bluprint to the app"""

    app.config.from_object(app_config[config_name])
    """We are loading the default configuration"""

    app.config.from_pyfile('config.py')

    db_uri = DataBaseConnection("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")
    try:
        if config_name == "testing":

            """Deletes all tables after tests have been run"""
            DataBaseConnection(db_uri).drop_all_tables()
            DataBaseConnection(db_uri).creat_tables()

        DataBaseConnection("dbname='kawalya' host='localhost' port=5432  user='kawalya' password='kawalyaa'").creat_tables()
    except ConnectionError:
        return ("connection error")

    return app
