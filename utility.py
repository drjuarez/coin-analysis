import time
from datetime import datetime
import calendar
import pdb

db_format = '%m-%d-%y %H:%M:%S'

def timestamp_for_db():
    now = time.localtime()
    return time.strftime(db_format, now)

def unix_timestamp_on(on_date):
    datetime_object = datetime.strptime(on_date, db_format)
    return calendar.timegm(datetime_object.timetuple())
