from flask import Flask, render_template
from flask import request
from flask import jsonify
import pymysql

app = Flask(__name__)

# 데이터베이스 연결 설정
def get_db_connection():
    connection = pymysql.connect(
        host='ros2database.c1y2m0kuy0ys.us-east-1.rds.amazonaws.com',  # RDS 엔드포인트
        user='icttest1220',      # 사용자 이름
        password='Icttest1220!!',  # 비밀번호
        db='ros2database'    # 데이터베이스 이름
    )
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # 데이터베이스에서 데이터 가져오기
    cursor.execute("SELECT * FROM trash_info")
    data = cursor.fetchall()
    
    connection.close()
    
    return render_template('index.html', data=data)



# # 로봇 로그 조회
# @app.route('/api/log/<int:robot_id>', methods=['GET'])
# def get_robot_log(robot_id):
#     response = {
#         'result': 'success',
#         'data': {
#             'id': robot_id,
#             'time': '',
#             'location': {
#                 'latitude': '',
#                 'longitude': '',
#             },
#             'battery': '',
#         },
#     }
#     return jsonify(response)

# # 분포도 조회
# @app.route('/api/log/<int:robot_id>', methods=['GET'])
# def get_trash_distribution(robot_id):
#     response = {
#         'result': 'success',
#         'data': [{
#             'robotId': robot_id,
#             'latlng': {
#                 'lat': '',
#                 'lng': '',
#             },
#             'time': '',
#             'trashType': '',
#         }]
#     }
#     return jsonify(response)

# # 시간별 쓰레기 수거 결과 조회
# @app.route('/api/log/<int:robot_id>', methods=['GET'])
# def get_trash_graph(robot_id):
#     response = {
#         'result': 'success',
#         'data': [{
#             'robotId': robot_id,
#             'latlng': {
#                 'lat': '',
#                 'lng': '',
#             },
#             'time': '',
#             'trashType': '',
#         }]
#     }
#     return jsonify(response)

# #테스트용
# @app.route('/api/test', methods=['GET'])
# def get_robot_log(robot_id):
#     response = {
#         'result': 'success',
#         'data': {
#             'test': 'ok'
#         }
#     }
#     return jsonify(response)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)