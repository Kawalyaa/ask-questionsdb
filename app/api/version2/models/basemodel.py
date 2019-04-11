from app.db_con import DataBaseConnection as db_con
from datetime import datetime, timedelta
import jwt
import os
KEY = os.getenv("SECRET")


class BaseModel(db_con):
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
                KEY,
                algorithm="HS256"
            ).decode('utf-8')
            resp = token
        except Exception as e:
            resp = e
        return resp

    def check_exists(self, table_name, field_name, value):
        con = self.init_db()
        cur = con.cursor()
        query = "SELECT * FROM {} WHERE {}='{}'".format(table_name, field_name, value)
        cur.execute(query)
        resp = cur.fetchone()
        con.commit()
        # resp = self.fetch_all_tables_rows(query)
        return resp is not None

    def blacklisted(self, blacklist, tokens, token):
        """This method gets access_tokens which have been blacklisted or used"""
        """Once acess_token have been generated they are kept in blacklist table"""
        if self.check_exists(blacklist, tokens, token) is True:
            return ("Token blacklisted")
        return ("new token")
        # query = """SELECT * FROM blacklist WHERE tokens = '{}';""".format(token)
        # get_one = self.fetch_single_data_row(query)
        # if get_one:
        #    return True
        # return False

    @staticmethod
    def decode_token(auth_token):
        """This function takes in an authtoken and decodes it, returning an integer or string"""
        # if self.blacklisted(auth_token) is True:
        #    return "Token has been blacklisted"
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

    def delete_tb_value(self, table_name, field_name, value):
        if self.check_exists(table_name, field_name, value) is False:
            return "Item not found"
        con = self.init_db()
        cur = con.cursor()
        query = "DELETE FROM {} WHERE {}={};".format(table_name, field_name, value)
        cur.execute(query)
        con.commit()
        # self.save_incoming_data_or_updates(query)
        return "Deleted"
