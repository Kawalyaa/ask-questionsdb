from contextlib import closing
from flask import current_app
import psycopg2
import os
from app.db_config import tables, destroydb
from app import creat_app


def connect_to():
    conn = psycopg2.connect("dbname='question_test' host='localhost' port=5432  user='kawalya' password='kawalyaa'")
    return conn


def init_test_db():
    con = connect_to()
    return con


def creat_tables():
    drop_all_tables()
    all_tables = tables()
    con = init_test_db()
    cur = con.cursor()
    for query in all_tables:
        cur.execute(query)
        con.commit()


def drop_all_tables():
    drop_all = destroydb()
    con = init_test_db()
    cur = con.cursor()
    for query in drop_all:
        cur.execute(query)
        con.commit()
