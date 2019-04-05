from werkzeug.exceptions import BadRequest
from app.api.version2.models.basemodel import BaseModel
from datetime import datetime


class PostModel(BaseModel):
    """class for post models inheriting from BaseModel"""
    def __init__(self, title='title', description='description', created_by=0):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_on = datetime.now()

    def check_exists(self, table_name, item_name, value):
        query = "SELECT * FROM {} WHERE {}='{}'".format(table_name, item_name, value)
        resp = self.fetch_single_data_row(query)
        return resp is not None

    def validate(self, the_input):
        for key, value in the_input.items():
            if not value:
                raise BadRequest("{} should not be empty".format(key))
            if key == "title":
                if isinstance(value, int):
                    raise BadRequest("{} value should be a string".format(key))
            if key == "description":
                if isinstance(value, int):
                    raise BadRequest("{} value should be a string".format(key))

    def save(self):
        """This method saves the post infomation"""
        posts = {
            "title": self.title,
            "description": self.description,
            "created_by": self.created_by
        }
        query = """INSERT INTO posts (title, description, created_by, created_on) VALUES \
         (%(title)s, %(description)s, %(created_by)s, ('now')) RETURNING post_id;"""
        id = self.save_and_return_id(query, posts)
        return id

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
            return ('Not found'), 404
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

    def update_question(self, title, description, post_id):
        if self.check_exists('posts', 'post_id', post_id) is False:
            return ("Not found"), 404

        query = "UPDATE posts SET title = '{}', description = '{}'\
        WHERE post_id = '{}';".format(title, description, post_id)
        self.save_incoming_data_or_updates(query)
        return "Updated"
