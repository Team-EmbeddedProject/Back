from datetime import timedelta

import db
import utils

def get_trash_distribution(robot_id, start_date, end_date):
    if not robot_id:
        return utils.format_error_response("robot_id is required.", 400)

    if not start_date or not end_date:
        return utils.format_error_response("start_date and end_date are required.", 400)
    
    try:
        start_date_dt = utils.get_datetime_date(start_date)
        end_date_dt = utils.get_datetime_date(end_date) + timedelta(days=1)

        condition = f"timestamp BETWEEN '{start_date_dt}' AND '{end_date_dt}'"
        robot_id_condition = utils.get_robot_id_condition(robot_id)
        if robot_id_condition:
            condition += " AND "+robot_id_condition
        
        rows = db.select_all(
            target="*",
            table="trash_info",
            condition=condition
        )

        if len(rows) == 0:
            return utils.format_response([])

        data = [{
            'robotId': row[2],
            'latlng': {'lat': row[4], 'lng': row[5]},
            'time': utils.format_datetime_full(row[1]),
            'trashType': row[3]
        } for row in rows if row[3] in ["plastic", "can", "pack"]]

        return utils.format_response(data)

    except Exception as e:
        return utils.format_error_response(e, 500)
