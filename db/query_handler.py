import pymysql

from .connection import get_connection

def get_select_query(target: str, table: str, condition: str | None):
    query = f"SELECT {target} FROM {table}"
    if condition:
        query += f" WHERE {condition}"
    return query

def execute_query(query: str):
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    except pymysql.MySQLError as e:
        print(f"[DB] error: {e}")
        return None

    finally:
        connection.close()

def select_all(target: str, table: str, condition: str | None = None):
    query = get_select_query(target, table, condition)
    return execute_query(query)

def select_one(target: str, table: str, condition: str | None = None):
    query = get_select_query(target, table, condition)
    results = execute_query(query)
    return results[0] if results else None
