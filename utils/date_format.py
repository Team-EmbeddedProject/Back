from datetime import datetime

def get_datetime_full(timestamp: str) -> datetime:
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

def get_datetime_date(timestamp: str) -> datetime:
    return datetime.strptime(timestamp, "%Y.%m.%d")

def format_datetime_full(timestamp: datetime):
    return timestamp.strftime("%Y.%m.%d %H:%M:%S")

def format_datetime_date(timestamp: datetime):
    return timestamp.strftime("%Y.%m.%d")