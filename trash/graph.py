from datetime import timedelta
from collections import defaultdict

import db
import utils

def get_trash_graph(robot_id, start_date, end_date):
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

        data_by_date = defaultdict(lambda: {'plastic': 0, 'pack': 0, 'can': 0, 'all': 0})
        for row in rows:
            date_str = utils.format_datetime_date(row[1])
            if row[3] in ["plastic", "pack", "can"]:
                data_by_date[date_str][row[3]] += 1
                data_by_date[date_str]['all'] += 1

        current_date = start_date_dt
        while current_date < end_date_dt:
            date_str = utils.format_datetime_date(current_date)
            data_by_date[date_str]
            current_date += timedelta(days=1)

        data = [{
            "time": date,
            "plastic": counts["plastic"],
            "pack": counts["pack"],
            "can": counts["can"],
            "all": counts["all"]
        } for date, counts in sorted(data_by_date.items())]

        return utils.format_response(data)

    except Exception as e:
        return utils.format_error_response(e, 500)
