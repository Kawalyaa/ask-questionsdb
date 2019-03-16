# from app.db_con import DataBaseConnection as db_con
from app.api.version2.models.basemodel import BaseModel
from datetime import datetime


class PostModel(BaseModel):
    """class for post models inheriting from BaseModel"""
    def __init__(self, title='title', description='description', created_by='created_by'):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_on = datetime.now()

    def check_exists(self, table_name, field_name, value):
        query = "SELECT * FROM {} WHERE {}='{}'".format(table_name, field_name, value)
        resp = self.fetch_all_tables_rows(query)
        return resp is not None

    def save(self):
        """This method saves the post infomation"""
        posts = {
            "title": self.title,
            "description": self.description,
            "created_by": self.created_by
        }
        if self.check_exists('posts', 'title', posts["title"]) is True:
            return "Post already exists"
        query = """INSERT INTO posts (title, description, created_by, created_on) VALUES \
         '{}', '{}', '{}', ('now')) RETURNING post_id;""".format(posts['title'], posts['description'], posts['created_by'])
        self.save_user_and_return_id(query)

    def get_posts(self):
        query = "SELECT * FROM posts;"
        data = self.fetch_all_tables_rows(query)
        res = []

        for i, items in enumerate(data):
            post_id, title, description, created_by, created_on = items
            posts = dict(
                post_id=post_id,
                title=title,
                description=description,
                created_by=int(created_by),
                created_on=str(created_on)
            )
        res.append(posts)
        return res

    def get_one_post(self, post_id):

        if self.check_exists('posts', 'post_id', post_id) is False:
            return ('Not found')
        query = "SELECT title, description, created_by, created_on FROM posts WHERE post_id={};".format(post_id)
        data = self.get_all_tb_rows_by_id(query)
        res = []

        posts = dict(
            title=data[0],
            description=data[1],
            created_by=int(data[2]),
            created_on=str(data[3])
        )
        res.append(posts)
        return res
