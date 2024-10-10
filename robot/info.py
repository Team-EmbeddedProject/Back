from flask import jsonify

import db
import utils
from config import ENV

def get_robot_info(robot_id):
    if not ENV["DATABASE"]["CONNECTION"]:
        return {
            'id': "1",
            'name': "A-01",
            'ip': "test"
        }

    row = db.select_one(
        target="*",
        table="robot",
        condition=f"id = {robot_id}"
    )

    if row:
        data = {
            'id': row[0],
            'name': row[1],
            'ip': row[2]
        }
        return data
    
    return None

def get_robots():
    if not ENV["DATABASE"]["CONNECTION"]:
       return utils.format_response( [
            {
            'id': "1",
            'name': "A-01",
            'ip': "test"
            },
            {
            'id': "2",
            'name': "A-02",
            'ip': "test"
            },
        ])
    
    try:
        rows = db.select_all(
            target="*",
            table="robot",
        )

        data = [{
            'id': row[0],
            'name': row[1],
            'ip': row[2]
        } for row in rows]

        return utils.format_response(data)
        
    except Exception as e:
        return utils.format_error_response(e, 500)