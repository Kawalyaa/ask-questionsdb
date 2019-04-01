from flask_restful import Resource
import yaml
import os
from flask import request, make_response, jsonify
from flasgger import swag_from
from app.api.version2.models.user_model import UserModel
from werkzeug.exceptions import BadRequest
import string
import re

KEY = os.getenv("SECRET")


def validate_user(user):
    """This function validates the user input and rejects or accepts it"""
    for key, value in user.items():
        # ensure keys have values
        if not value:
            raise BadRequest("{} is lacking. It is required field".format(key))
        # validate length
        if key == "user_name":
            if len(value) < 4:
                raise BadRequest("The {} provided is too short, it should be 5 characters above".format(key))
            elif len(value) > 15:
                raise BadRequest("The {} provided is too long, it should be less than 15 characters".format(key))
        if key == "password":
            if len(value) < 4:
                raise BadRequest("The {} provided is too short, it should be 5 characters above".format(key))
            elif len(value) > 18:
                raise BadRequest("The {} provided is too long, it should be less than 18 characters".format(key))

        if key == "name":
            # make sure the value provided is a string
            for i in value:

                if i not in string.ascii_letters:
                    raise BadRequest("{} can not have non alphatic characters".format(key))
        if key == "email":
            # make sure email contains expetected characters
            if not re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', value):
                raise BadRequest("The email provided is invalid")


class Auth(Resource):
    """class to handle user login"""

    @swag_from('../docs/login.yml')
    def post(self):
        req = request.get_json()
        if not req:
            return jsonify({"message": "Content should be json"})
        user_name = req['user_name']
        password = req['password']

        login = {
            "user_name": user_name,
            "password": password
        }
        validate_user(login)
        res = UserModel().check_exists(login['user_name'])
        if res is False:
            return make_response(jsonify({
                "message": "No user found"
            }), 401)
        record = UserModel().get_user_by_username(login['user_name'])
        user_id, password = record
        # our user name has got the password and the user_id
        # This means if login['user_name'] == user_name in table, record or user_name has user_id, password
        if password != login['password']:
            return make_response(jsonify({
                "message": "user_name and password does not much"
            }), 401)
        token = UserModel().ecnode_token(user_id)
        return make_response(jsonify({
            "message": "Welcome {}".format(login['user_name']),
            "access_token": str(token)
        }), 200)


class AuthLogOut(Resource):
    """class to handle user logout"""

    def post(self):
        auth = request.headers.get('Authorization')
        if not auth:
            return make_response(jsonify({
                "message": "No authorization header provided. This resource is secured"
            }), 403)
        auth_t_oken = auth.split(" ")[1]
        response = UserModel().decode_token(auth_t_oken)
        if isinstance(response, int):
            UserModel().logout(auth_t_oken)
            return make_response(jsonify({
                ""
                "message": "Loged out successfully"
            }), 200)
        return make_response(jsonify({
            "message": response
        }), 401)


class Registration(Resource):
    """class to register new user"""

    @swag_from('../docs/signup.yml')
    def post(self):
        req = request.get_json()

        if not req:
            return jsonify({"mesage": "Content should be json"})
        try:
            name = req['name'].strip()
            email = req['email'].strip()
            password = req['password'].strip()
            user_name = req['user_name'].strip()
        except ValueError:
            return jsonify({"message": "Incorect input"})
        # if not re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
        #    return make_response(jsonify({"Message": "The email provided is invalid"}), 400)
        new = {
            "name": name,
            "email": email,
            "password": password,
            "user_name": user_name
        }
        validate_user(new)
        requester = UserModel(**new)
        res = requester.save_user()
        # save user and return id
        if isinstance(res, int):
            user_id = res
            token = UserModel.ecnode_token(user_id)
            return make_response(jsonify({
                "message": "created successfully",
                "access_token": str(token),
                "user_id": user_id
            }), 201)

        return make_response(jsonify({
            "message": "User exists"}), 409)
