from datetime import datetime, timedelta

def get_today() -> str:
    return datetime.today().strftime('%Y-%m-%d')

def days_between(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)

def add_days(date: str, days: int) -> str:
    d = datetime.strptime(date, '%Y-%m-%d')
    new_date = d + timedelta(days=days)
    return new_date.strftime('%Y-%m-%d')

def is_weekend(date: str) -> bool:
    d = datetime.strptime(date, '%Y-%m-%d')
    return d.weekday() >= 5

def format_date(date: str, format: str) -> str:
    d = datetime.strptime(date, '%Y-%m-%d')
    return d.strftime(format)
