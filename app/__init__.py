from flask import Flask
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

    db_url = app_config[config_name].DATABASE_URL

    # Print which database is being used in a given environment
    print("\n\n\n", db_url, "\n\n\n")

    DataBaseConnection(db_url)
    # which has the db_url as its instance variable for connectio
    if config_name == "testing":
        """Deletes all tables after tests have been run"""
        DataBaseConnection.drop_all_tables(DataBaseConnection)
    DataBaseConnection.creat_tables(DataBaseConnection)

    return app
