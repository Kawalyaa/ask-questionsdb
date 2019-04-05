from flask import Flask
from flasgger import Swagger
# from flask_cors import CORS
from instance.config import app_config
# from app.db_con import DataBaseConnection
from app.api.version2 import ver2 as v2
from app.db_con import DataBaseConnection


# def url_for_testing(url=DataBaseConnection("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")):

#    url.drop_all_tables()
#    url.creat_tables()


# def url_for_dev(url=DataBaseConnection("dbname='kawalya' host='localhost' port=5432  user='kawalya' password='kawalyaa'")):
# url connection for decelopment
#    url.creat_tables()
#    url.conn()
#    url.cursor()


def creat_app(config_name):
    """This method creats app with configuration in the instance folder"""
    # We will be using the config variable to determine the database

    app = Flask(__name__, instance_relative_config=True)
    """using instance_relative_config will load config file from instance folder when app created"""
    """Loading the configurations from config.py contained in the instance folder"""
    # CORS(app)
    app.register_blueprint(v2)
    """Registering blueprint to the app"""
    # name_space = app.namespace()

    app.config['SWAGGER'] = {'uiversion': 2, 'title': 'askquestiondb',
                             'description': "is a web based app that enables users to \
                             ask questions on the platform and get answers.",
                             'basePath': '', 'version': '2.0.1'}
    Swagger(app)

    app.config.from_object(app_config[config_name])
    """We are loading the default configuration"""

    app.config.from_pyfile('config.py')
    DataBaseConnection().creat_tables()
    # Loading db_connection
    # if config_name == "development":
    #    url_for_testing()
    # url_for_dev()
    return app
