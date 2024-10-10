def get_robot_id_condition(robot_id: str):
    return None if robot_id == "all" else f"robot_id = {robot_id}"
