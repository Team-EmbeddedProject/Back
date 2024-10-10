import socket
import threading

from config import ENV
import utils

from ..info import get_robot_info

robot_connections = {}
REMOTE_MODE = ENV["ROBOT"]["CONNECTION"]

def isConnected(robot_id):
    return robot_id in robot_connections

def create_robot_connection(robot_id, ip="155.230.25.109", port=3000):
    try:
        if REMOTE_MODE:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            robot_connections[robot_id] = sock
        else:
            robot_connections[robot_id] = robot_id
        print(f"[ROBOT] 로봇 {robot_id}와 연결됨")
        return f"{robot_id} 로봇 연결"
    except Exception as e:
        return str(e)

def connect_robot(robot_id, ip="155.230.25.109", port=3000):
    try:
        if not isConnected(robot_id):
            if REMOTE_MODE:
                robot = get_robot_info(robot_id)
                robot_ip = robot['ip']
            else:
                robot_ip = ip

            thread = threading.Thread(target=create_robot_connection, args=(robot_id, robot_ip, port))
            thread.start()
            
            return utils.format_response("")
        else:
            return utils.format_error_response(robot_id+" 로봇에 연결할 수 없습니다.")
    except Exception as e:
        return utils.format_error_response(e)

def handle_robot_connection(robot_id, code):
    try:
        sock = robot_connections[robot_id]

        if REMOTE_MODE:
            sock.sendall(code.encode("utf-8"))
        print(f"[ROBOT] 로봇 {robot_id}로 명령 전송: {code}")

        if REMOTE_MODE:
            response = sock.recv(1024).decode("utf-8")
            print(f"[ROBOT] 로봇 {robot_id} 응답 수신: {response}")

        if code == "000":
            if REMOTE_MODE:
                sock.close()
            del robot_connections[robot_id]
            print(f"[ROBOT] 로봇 {robot_id}와 연결 종료")

        if REMOTE_MODE:
            return response
        else:
            return code

    except Exception as e:
        print(f"로봇 {robot_id}와 통신 중 오류 발생: {e}")
        if robot_id in robot_connections:
            if REMOTE_MODE:
                robot_connections[robot_id].close()
            del robot_connections[robot_id]
        return None

def delete_connections():
    for sock in robot_connections:
        if REMOTE_MODE:
            sock.sendall("000".encode("utf-8"))
            response = sock.recv(1024).decode("utf-8")
            print(f"[ROBOT] {sock} 응답 수신: {response}")
            sock.close()
        print(f"[ROBOT] {sock} 연결 종료")
