# from app.db_con import DataBaseConnection as db_con
from app.api.version2.models.basemodel import BaseModel


class UserModel(BaseModel):
    """class for user models inheriting from BaseModel"""
    def __init__(self, name='name', email='email', password='password', user_name='user_name'):
        self.name = name
        self.email = email
        self.password = password
        self.user_name = user_name

    def check_exists(self, username):
        """Check if the records exist"""
        query = "SELECT * FROM users WHERE user_name = '%s'" % (username)
        data = self.fetch_single_data_row(query)
        return data is not None

    def save_user(self):
        """This method saves the user infomation"""
        user = {
            "name": self.name,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password
        }

        query = """INSERT INTO users (name, user_name, email, password) VALUES \
        (%(name)s, %(user_name)s, %(email)s, %(password)s) RETURNING user_id"""
        if self.check_exists(user['user_name']) is True:
            return("User already exists")
        id = self.save_and_return_id(query, user)
        return int(id)

        # executing aquery and user into a table
        # user_id = cur.fetchone()[0]
        # con.commit()
        # save changes to the DATABASE_URL
        # con.close()
        # return user_id

    def logout(self, token):
        """This method keeps used tokens in the blacklist table"""
        query = "INSERT INTO blacklist (tokens) VALUES ('{}');".format(token)
        self.save_incoming_data_or_updates(query)

    def get_user_by_username(self, user_name):
        query = """SELECT user_id, password \
        FROM users WHERE user_name = '{}'""".format(user_name)
        user_info = self.fetch_single_data_row(query)
        return user_info
