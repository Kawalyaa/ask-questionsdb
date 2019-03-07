from app.db_config import init_db
from datetime import datetime, timedelta
import jwt
import os
# fr# om flask import current_app, g


class BaseModel(object):
    """class to stracture the user"""
    @staticmethod
    def ecnode_token(user_id):
        """Generating the auth token returning a string"""
        try:
            payload = {
                # Token expiry date
                "exp": datetime.utcnow() + timedelta(minutes=30),
                # The time token is generated
                "iat": datetime.utcnow(),
                # User to be idenfied
                "user": user_id
            }
            token = jwt.encode(
                payload,
                os.getenv("SECRET"),
                algorithm="HS256"
            ).decode('utf-8')
            resp = token
        except Exception as e:
            resp = e

        return resp

    def blacklisted(self, token):
        """This method gets access_tokens which have been blacklisted or used"""
        """Once acess_token have been generated they are kept in blacklist table"""
        con = init_db()
        cur = con.cursor()
        query = """SELECT FROM blacklist WHERE tokens = %s;"""
        cur.execute(query, [token])
        if cur.fetchone():
            return True
        return False

    def decode_token(self, auth_token):
        """This function takes in an authtoken and decodes it, returning an integer or string"""
        if self.blacklisted(auth_token):
            return "Token has been blacklisted"
        secret = os.getenv("SECRET")
        try:
            payload = jwt.decode(auth_token, secret)
            # We decode the auth_token using the same secret key used to encode it
            # If it is valid we get or the user_id from the "user" index of payload
            return payload['user']  # user_id
        except jwt.ExpiredSignatureError:
            return "The token has expired"
        except jwt.InvalidTokenError:
            return "The token is invalid"

    def check_exist(self, table_name, field_name, value):
        con = init_db()
        cur = con.cursor()
        query = "SELECT * FROM {} WHERE {}='{}'".format(table_name, field_name, value)
        cur.execute(query)
        resp = cur.fetchall()
        if resp:
            return True
        else:
            return False

    def delete_tb_value(self, table_name, field_name, value):
        if self.check_exist(table_name, field_name, value) is False:
            return "Item not found"
        con = init_db()
        cur = con.cursor()
        query = "DELETE FROM {} WHERE {}={}".format(table_name, field_name, value)
        cur.execute(query)
        con.commit()
        con.close()
        return "Deleted"

    def update_question(self, title, description, post_id):
        if self.check_exist('posts', 'post_id', post_id) is False:
            return "Not found"
        con = init_db()
        cur = con.cursor()
        query = "UPDATE posts SET title = (%s), description = (%s)\
        WHERE post_id = (%s) ;"
        # .format(table_name, field_name, data, item_p, item_id)
        cur.execute(query, (title, description, post_id))
        con.commit()
        con.close()
        return "Updated"
