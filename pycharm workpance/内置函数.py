class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self._month = month
        self.year = year
    # 类方法
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date = cls(day, month, year)
        return date
    # 静态方法
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999
    # 把方法当做属性
    @property
    def month(self):
        """month (1-12)"""
        return self.day

if __name__ == '__main__':
   i = Date("13","2","2012")
   print(i.month)
   print(Date.is_date_valid("13-2-2013"))
   a= Date.from_string("25-8-2013")
   print(a.month)