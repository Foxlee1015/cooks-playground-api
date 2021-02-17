import traceback

import pymysql
from contextlib import contextmanager


db_host = "211.209.41.120"
db_port = 16936
db_user = "root"
db_pw = "1234"
db_dataset = 'cpg'
db_charset = 'utf8'


@contextmanager
def get_db():
    try:
        conn = None
        conn = pymysql.connect(
            host=db_host, port=db_port, user=db_user, password=db_pw, db=db_dataset, 
            charset=db_charset, cursorclass=pymysql.cursors.DictCursor)
        yield conn
    except:
        traceback.print_exc()
    finally:
        conn.close()
        pass


def init_db():
    with get_db() as conn:
        from core import schema
        sql_list= schema.schema.split(";")
        for sql in sql_list:
            if sql != '' and sql != '\n':
                try:
                    conn.cursor().execute(sql)
                except:
                    traceback.print_exc()
        conn.commit()


def insert_user(user_name, email, user_type):
    try:
        with get_db() as conn:

            cur = conn.cursor()
            sql = "INSERT into user(name, email, user_type) values (%s,%s,%s)"
            cur.execute(sql, (user_name, email, user_type))
            conn.commit()

        return True
    except:
        traceback.print_exc()
        return False


def get_users():
    try:
        with get_db() as conn:

            cur = conn.cursor()
            sql = """
                SELECT *
                FROM user
            """
            cur.execute(sql)
            conn.commit()
            res = cur.fetchall()

        return res
    except:
        traceback.print_exc()
        return False
    

def delete_users(user_ids):
    """
    :param user_ids: a list of user ids
    """
    try:
        with get_db() as conn:

            cur = conn.cursor()

            sql = f"""
                DELETE FROM user
                WHERE id in ({','.join(str(user_Id) for user_id in user_ids)})
            """
            cur.execute(sql)
            conn.commit()

        return True
    except:
        traceback.print_exc()
        return False