from flask import Flask
from flask import request
from flask_cors import CORS
import signal
import sys

import robot
import trash
import analyze

app = Flask(__name__)
CORS(app)

# 로봇 목록
@app.route('/api/robots', methods=['GET'])
def api_robots():
    return robot.get_robots()

# 원격 제어 명령 전달
@app.route('/api/remote/control', methods=['POST'])
def api_remote_control():
    data = request.json
    robot_id = data.get('robot_id')
    code = data.get('code')
    return robot.control_robot(robot_id=robot_id, code=code)

# 원격 제어 연결
@app.route('/api/remote/connect', methods=['POST'])
def api_remote_connect():
    data = request.json
    robot_id = data.get('robot_id')
    return robot.connect_robot(robot_id)

# 로봇 로그 조회
@app.route('/api/log/<string:robot_id>', methods=['GET'])
def api_log(robot_id):
    return robot.get_log(robot_id)

# 로봇 로그 조회 - 기간
@app.route('/api/log/period/<string:robot_id>', methods=['GET'])
def api_log_period(robot_id):
    return robot.get_log_period(robot_id)

# 쓰레기 수거 결과 조회 - 기간
@app.route('/api/trash/period/<string:robot_id>', methods=['GET'])
def api_trash_period(robot_id):
    return trash.get_period(robot_id)

# 쓰레기 수거 결과 분포도 조회
@app.route('/api/trash/distribution/', methods=['GET'])
def api_trash_distribution():
    robot_id = request.args.get('robot_id')
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')
    return trash.get_distribution(robot_id, start_date, end_date)

# 시간별 쓰레기 수거 결과 조회
@app.route('/api/trash/graph/', methods=['GET'])
def api_trash_graph():
    robot_id = request.args.get('robot_id')
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')
    return trash.get_graph(robot_id, start_date, end_date)

# 분석 결과 조회 - 쓰레기 양
@app.route('/api/analyze/amount', methods=['GET'])
def api_analyze_amount():
    return analyze.get_amount()

# 분석 결과 조회 - 전월 대비 변화량
@app.route('/api/analyze/change', methods=['GET'])
def api_analyze_change():
    return analyze.get_change()


# 종료(컨트롤 C)
def signal_handler(sig, frame):
    robot.delete_connections()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    try:
        app.run('0.0.0.0', port=5000, debug=True, threaded=True)
    
    except Exception as e:
        print(e)
    
    finally:
        robot.delete_connections()