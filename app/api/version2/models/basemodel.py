from app.db_config import init_db


class BaseModel(object):
    """class to stracture the user questions"""
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
        return "Updated"
