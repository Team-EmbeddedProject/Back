import db
import utils

def get_robot_log(robot_id):
    try:
        rows = db.select_all(
            target = "*",
            table = "robot_log",
            condition = utils.get_robot_id_condition(robot_id)
        )
        sorted_rows = sorted(rows, key=lambda row: row[1], reverse=True)

        data = [
            {
                'id': row[2],
                'time': utils.format_datetime_full(utils.get_datetime_full(row[1])),
                'location': {
                    'row': row[3],
                    'column': row[4],
                }
            }
            for row in sorted_rows if row[2]
        ]

        return utils.format_response(data)
        
    except Exception as e:
        return utils.format_error_response(e, 500)