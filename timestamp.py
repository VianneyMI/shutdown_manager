from datetime import datetime
class  Timestamp:
    def __init__(self,date=None,time=None):
        self.date=date
        self.time=time

    def set_date(self,date):
        self.date=date

    def set_time(self,time):
        self.time=time

    def to_datetime(self):
        return datetime(self.date.year, self.date.month, self.date.day,int(self.time.split(':')[0]),int(self.time.split(':')[1]))

    def to_seconds(self):
        seconds=self.to_datetime().timestamp()
        return seconds
