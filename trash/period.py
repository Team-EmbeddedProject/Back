import db
import utils

def get_trash_period(robot_id):
    try:
        row = db.select_one(
            target="MIN(timestamp) AS min_time, MAX(timestamp) AS max_time",
            table="trash_info",
            condition=utils.get_robot_id_condition(robot_id)
        )

        if not row[0] or not row[1]:
            return utils.format_response(None)

        data = {
            'start_time': utils.format_datetime_date(row[0]),
            'end_time': utils.format_datetime_date(row[1])
        }

        return utils.format_response(data)

    except Exception as e:
        return utils.format_error_response(e, 500)
