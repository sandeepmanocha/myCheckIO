import datetime as dt

'''
0   Monday
1   Tuesday 
2   Wednesday 
3   Thursday 
4   Friday 
5   Saturday
6   Sunday
'''
def checkio(year):

    black_friday = 0
    for month in range(1,13):
        if dt.datetime(year,month,13,0,0).weekday() == 4:
            black_friday += 1

    return black_friday


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
