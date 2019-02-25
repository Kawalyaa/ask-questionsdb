import psycopg2
import os
# host = 'localhost'
# user = 'kawalya'
# port = 5432
# password = 'kawalyaa'
# dbname = 'questions'
# conn_url="dbname='questions' host='localhost' port=5432  user='kawalya' password='kawalyaa'"

uri = os.getenv('DATABASE_URL')

test_uri = os.getenv('DATABASE_TEST_URL')


def connection(url):
    """This method returns connection"""
    con = psycopg2.connect(url)
    return con


def init_db():
    """ This method returns connection and creates tables"""
    con = connection(uri)
    cur = con.cursor()
    queries = tables()
    for query in queries:
        cur.execute(query)
    con.commit()
    return con


def init_test_db(test_url):
    """returns connection and create tables for testing"""
    con = connection(test_uri)
    cur = con.cursor()
    queries = tables()
    for query in queries:
        cur.execute(query)
    con.commit()
    return con


def destroy():
    """Deletes all tables after tests have been run"""
    con = connection(test_uri)
    cur = con.cursor()

    posts = """DROP TABLE IF EXISTS posts CASCADE;"""
    users = """DROP TABLE IF EXISTS users CASCADE;"""
    blacklist = """DROP TABLE IF EXISTS blacklist CASCADE;"""

    queries = [posts, users, blacklist]

    for query in queries:
        cur.execute(query)
    con.commit()
    return con


def tables():
    """ Contains all tables creation queries"""
    users = """ CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    name character varying (50) NOT NULL,
    user_name character varying (50) NOT NULL,
    email character varying (50) NOT NULL,
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
    password character varying (15) NOT NULL
    );"""

    posts = """ CREATE TABLE IF NOT EXISTS posts (
    post_id serial PRIMARY KEY NOT NULL,
    title varchar (50) NOT NULL,
    description varchar (200) NOT NULL,
    created_by varchar (100) NOT NULL,
    created_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""

    blacklist = """CREATE TABLE IF NOT EXISTS blacklist (
    tokens character varying(200) NOT NULL
    ); """

    queries = [users, posts, blacklist]
    return queries
