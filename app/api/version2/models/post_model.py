from app.db_config import init_db
from app.api.version2.models.basemodel import BaseModel


class PostModel(BaseModel):
    """class for post models inheriting from BaseModel"""
    def __init__(self, title, description, created_by):
        self.title = title
        self.description = description
        self.created_by = created_by

    def save(self):
        """This method saves the post infomation"""
        posts = {
            "title": self.title,
            "description": self.description,
            "created_by": self.created_by
        }

        con = init_db()
        """connect to db and create tables using  imported init_db function"""

        cur = con.cursor()
        """Execute psql statements we shall be using it always to execute statements"""
        if BaseModel().check_exist('posts', 'title', self.title) is True:
            return "Post already exists"
        query = """INSERT INTO posts (title, description, created_by) VALUES \
        (%(title)s, %(description)s, %(created_by)s) RETURNING user_id"""

        cur.execute(query, posts)
        # Do what the query  says and substitute the values for posts into the table
        # executing aquery or enter fata into posts tables l 26
        post_id = cur.fetchone()[0]
        con.commit()
        # save changes to the DATABASE_URL
        con.close()
        return post_id

    def get_posts(self):
        con = init_db()
        cur = con.cursor()
        query = "SELECT title, description, created_by, post_id, created_on FROM posts;"
        cur.execute(query)
        data = cur.fetchall()
        res = []

        for i, items in enumerate(data):
            title, description, created_by, post_id, created_on = items
            posts = dict(
                post_id=int(post_id),
                title=title,
                description=description,
                created_by=int(created_by),
                created_on=str(created_on)
            )
            res.append(posts)
            return res

    def get_one_post(self, post_id):
        con = init_db()
        cur = con.cursor()
        if BaseModel().check_exist('posts', 'post_id', post_id) is False:
            return ('Not found')
        query = "SELECT title, description, created_by, created_on FROM posts WHERE post_id={};".format(post_id)
        cur.execute(query)
        data = cur.fetchall()[0]
        # fetch all values from one culom where post_id == post_id in get_one_post
        res = []

        posts = dict(
            title=data[0],
            description=data[1],
            created_by=int(data[2]),
            created_on=str(data[3])
        )
        res.append(posts)
        return res
