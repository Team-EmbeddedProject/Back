from flask import jsonify

import utils

from ..info import get_robot_info
from .connection import handle_robot_connection, isConnected

def control_robot(robot_id:str, code:str):
    if not robot_id or not code:
        return utils.format_error_response("robot_id and code are required.", 400)

    try:
        if not isConnected(robot_id):
            return utils.format_error_response(f"{robot_id} 로봇과 연결되어 있지 않습니다.", 500)

        response = handle_robot_connection(robot_id, code)
        if response is None:
            return utils.format_error_response("로봇과의 통신 실패")
        
        return jsonify({'result': 'success', 'message': f'로봇 응답: {response}'})
    except Exception as e:
        return utils.format_error_response(e)
