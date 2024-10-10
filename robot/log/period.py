import db
import utils

def get_robot_log_period(robot_id):
    try:
        row = db.select_one(
            target="MIN(timestamp) AS min_time, MAX(timestamp) AS max_time",
            table="robot_log",
            condition=utils.get_robot_id_condition(robot_id)
        )

        data = {
            'start_time': utils.format_datetime_date(utils.get_datetime_full(row[0])),
            'end_time': utils.format_datetime_date(utils.get_datetime_full(row[1]))
        }

        return utils.format_response(data)

    except Exception as e:
        return utils.format_error_response(e, 500)