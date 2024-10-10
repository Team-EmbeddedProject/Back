import utils
import db

def get_analyze_change():
    try:
        rows = db.select_all(
            target="*",
            table="analyze_info",
            condition="total_percentage IS NOT NULL"
        )

        if len(rows) == 0:
            return utils.format_response([])
        
        data = []
        for row in rows:
            if row[6]:
                data.append(
                    {
                        'time': str(row[7])+"."+str(row[1]).zfill(2)+" "+str(row[6])+"주차",
                        'change': row[5]
                    })
    

        return utils.format_response(data)
    
    except Exception as e:
        return utils.format_error_response(e, 500)