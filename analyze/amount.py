from collections import defaultdict

import db
import utils

def get_analyze_amout():
    try:
        rows = db.select_all(
            target="*",
            table="analyze_info"
        )

        if len(rows) == 0:
            return utils.format_response([])
        
        data_by_date = defaultdict(lambda: {'plastic': 0, 'paper': 0, 'can': 0, 'rubber':0, 'glass':0, 'all': 0})

        for row in rows:
            date_str = str(row[7])+"."+str(row[1]).zfill(2)
            data_by_date[date_str][row[2]] += row[4]
            data_by_date[date_str]['all'] += row[4]

        data = [{
            "time": date,
            "plastic": counts["plastic"],
            "paper": counts["paper"],
            "can": counts["can"],
            "rubber": counts["rubber"],
            "glass": counts["glass"],
            "all": counts["all"]
        } for date, counts in sorted(data_by_date.items())]

        return utils.format_response(data)
    
    except Exception as e:
        return utils.format_error_response(e, 500)