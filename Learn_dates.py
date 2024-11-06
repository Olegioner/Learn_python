from datetime import date, timedelta

def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    dates = [date.fromordinal(i) for i in range(date.toordinal(start), date.toordinal(end)+1)]
    return sum(map(lambda x: 1 if x.weekday() == 5 else 0, dates))


date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))