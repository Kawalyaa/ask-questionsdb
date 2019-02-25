from app.db_config import init_db
from app.api.version2.models.basemodel import BaseModel


class UserModel(BaseModel):
    """class for user models inheriting from BaseModel"""
    def __init__(self, name='name', email='email', password='password', user_name='user_name'):
        self.name = name
        self.email = email
        self.password = password
        self.user_name = user_name

    def save(self):
        """This method saves the user infomation"""
        user = {
            "name": self.name,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password
        }

        con = init_db()
        """connect to db and create tables using  imported init_db function"""

        cur = con.cursor()
        """Execute psql statements we shall be using it always to execute statements"""
        if BaseModel().check_exist('users', 'email', self.email) is True:
            return "User already existsI!"
        query = """INSERT INTO users (name, user_name, email, password) VALUES \
        (%(name)s, %(user_name)s, %(email)s, %(password)s) RETURNING user_id"""

        cur.execute(query, user)
        # executing aquery and user into a table
        user_id = cur.fetchone()[0]
        con.commit()
        # save changes to the DATABASE_URL
        con.close()
        return user_id

    def logout(self, token):
        con = init_db()
        cur = con.cursor()
        query = "INSERT INTO blacklist (tokens) VALUES ('{}');".format(token)
        cur.execute(query)
        con.commit()
        con.close()

    def get_user_by_username(self, user_name):
        con = init_db()
        cur = con.cursor()
        query = """SELECT user_id, password \
        FROM users WHERE user_name = '{}'""".format(user_name)
        cur.execute(query)
        data = cur.fetchone()
        cur.close()
        return data
