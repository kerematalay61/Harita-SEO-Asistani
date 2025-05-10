import uuid
import datetime

def generate_id():
    return str(uuid.uuid4())

def format_datetime(dt=None):
    if not dt:
        dt = datetime.datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")
