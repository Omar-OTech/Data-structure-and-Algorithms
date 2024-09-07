class Solution(object):
    def daysBetweenDates(self, date1, date2):
        def isLeapYear(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        def daysInMonth(year, month):
            if month == 2:
                return 29 if isLeapYear(year) else 28
            elif month in [4, 6, 9, 11]:
                return 30
            else:
                return 31
        def daysSinceEpoch(year, month, day):
            days = 0
            for y in range(1971, year):
                days += 366 if isLeapYear(y) else 365
            for m in range(1, month):
                days += daysInMonth(year, m)
            return days + day - 1
        date1 = list(map(int, date1.split("-")))
        date2 = list(map(int, date2.split("-")))
        return abs(daysSinceEpoch(date1[0], date1[1], date1[2]) - daysSinceEpoch(date2[0], date2[1], date2[2]))

# test code
s = Solution()
print(s.daysBetweenDates("2019-06-29", "2019-06-30")) # 1
print(s.daysBetweenDates("2020-01-15", "2019-12-31")) # 15
print(s.daysBetweenDates("2019-06-29", "2019-06-29")) # 0
print(s.daysBetweenDates("2020-01-15", "2020-01-15")) # 0
print(s.daysBetweenDates("2020-01-15", "2020-01-16")) # 1
print(s.daysBetweenDates("2020-01-15", "2020-01-17")) # 2
print(s.daysBetweenDates("2020-01-15", "2020-01-18")) # 3
print(s.daysBetweenDates("2020-01-15", "2020-01-19")) # 4
print(s.daysBetweenDates("2020-01-15", "2020-01-20")) # 5
print(s.daysBetweenDates("2020-01-15", "2020-01-21")) # 6