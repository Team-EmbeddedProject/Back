aws_db = {
    "user": "icttest1220",
    "password": "Icttest1220!!",
    "host": "ros2database.c1y2m0kuy0ys.us-east-1.rds.amazonaws.com",
    "port": "3306", # Maria DB의 포트
    "database": "ros2database",
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{aws_db['user']}:{aws_db['password']}@{aws_db['host']}:{aws_db['port']}/{aws_db['database']}?charset=utf8"
