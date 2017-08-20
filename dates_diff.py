import datetime as dt

def days_diff(date1, date2):
    retval = 0
    dt1 = dt.datetime(date1[0],date1[1],date1[2])
    dt2 = dt.datetime(date2[0], date2[1], date2[2])
    retval = dt1 - dt2

    return abs(retval.days)

if __name__ == '__main__':
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
