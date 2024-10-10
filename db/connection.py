import pymysql

from config import ENV

def get_connection():
    return pymysql.connect(
        host=ENV["DATABASE"]["HOST"],
        user=ENV["DATABASE"]["USER"],
        password=ENV["DATABASE"]["PW"],
        db=ENV["DATABASE"]["DB"]
    )
