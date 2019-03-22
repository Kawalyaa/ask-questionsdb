import psycopg2
from app.db_config import tables, destroydb


class DataBaseConnection:
    """ Handles the main connection to the database of the app setting """

    def __init__(self, db_url):
        """ initialize the class instance to take a database url as a parameter"""
        try:
            global con, cur
            con = psycopg2.connect(db_url)
            cur = con.cursor()
        except Exception as error:
            print(error)

    def creat_tables(self):
        all_tables = tables()
        for query in all_tables:
            cur.execute(query)
            con.commit()

    def drop_all_tables(self):
        drop_all = destroydb()
        for query in drop_all:
            cur.execute(query)
            con.commit()

    def fetch_single_data_row(self, query):
        """ retreives a single row of data from a table """
        cur.execute(query)
        fetchedRow = cur.fetchone()
        con.commit()
        return fetchedRow

    def save_incoming_data_or_updates(self, query):
        """ saves data passed as a query to the stated table """
        cur.execute(query)
        con.commit()

    def fetch_all_tables_rows(self, query):
        """ fetches all rows of data store """
        cur.execute(query)
        all_data_rows = cur.fetchall()
        return all_data_rows

    def save_user_and_return_id(self, query, user):
        """get the user id"""
        cur.execute(query, user)
        user_id = cur.fetchone()[0]
        con.commit()
        return int(user_id)

    def save_post_and_return_id(self, query, posts):
        """get the user id"""
        cur.execute(query, posts)
        user_id = cur.fetchone()[0]
        con.commit()
        return int(user_id)

    def get_all_tb_rows_by_id(self, query):
        """return all rows by id"""
        cur.execute(query)
        id = cur.fetchall()[0]
        # fetch all values from one culom where post_id == post_id in get_one_post
        # self.con.commit()
        return id
