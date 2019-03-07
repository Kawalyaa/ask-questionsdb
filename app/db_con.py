import psycopg2


def init_tdb():
    """returns connection and create tables for testing"""
    con = psycopg2.connect("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")

    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    name character varying (50) NOT NULL,
    user_name character varying (50) NOT NULL,
    email character varying (50) NOT NULL,
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
    password character varying (15) NOT NULL
    );""")
    cur.execute(""" CREATE TABLE IF NOT EXISTS posts (
    post_id serial PRIMARY KEY NOT NULL,
    title varchar (50) NOT NULL,
    description varchar (200) NOT NULL,
    created_by varchar (100) NOT NULL,
    created_on timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS blacklist (
    tokens character varying(200) NOT NULL
    ); """)

    con.commit()
    return con


def destroydb():
    """Deletes all tables after tests have been run"""
    con = psycopg2.connect("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")
    cur = con.cursor()

    posts = """DROP TABLE IF EXISTS posts CASCADE;"""
    users = """DROP TABLE IF EXISTS users CASCADE;"""
    blacklist = """DROP TABLE IF EXISTS blacklist CASCADE;"""
    queries = [posts, users, blacklist]
    try:
        for query in queries:
            cur.execute(query)
        con.commit()
    except ConnectionError:
        print("Failed")
