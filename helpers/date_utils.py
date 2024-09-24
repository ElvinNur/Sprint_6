from datetime import datetime, timedelta

def get_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return future_date.strftime('%d.%m.%Y')