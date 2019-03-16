# import psycopg2
# import os

# uri = os.getenv('DATABASE_URL')

# test_uri = os.getenv('DATABASE_TEST_URL')


# def connection(url):
#    """This method returns connection"""
#    con = psycopg2.connect('')
#    return con


# def init_db():
#    """ This method returns connection and creates tables"""
#    con = connection(uri)
#    cur = con.cursor()
#    queries = tables()
#    for query in queries:
#        cur.execute(query)
#    con.commit()
#    return con


def destroydb():
    """Deletes all tables after tests have been run"""

    posts = """DROP TABLE IF EXISTS posts CASCADE;"""
    users = """DROP TABLE IF EXISTS users CASCADE;"""
    blacklist = """DROP TABLE IF EXISTS blacklist CASCADE;"""
    return[posts, users, blacklist]


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
    return[users, posts, blacklist]
