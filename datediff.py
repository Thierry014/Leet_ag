from datetime import date, timedelta, datetime


f = date(2014, 12, 31) # 31 december 2014
s = date(2011, 1, 1) # 1 january 2011


print((f-s).days)




def sum_light(els) -> int:
    """
        how long the light bulb has been turned on
    """
    print(els)
    total = 0
    for i in range(1,len(els),2):
        print(i)
        temp = (els[i]-els[i-1]).seconds
        if (els[i]-els[i-1]).days >0:
            temp += 60*60*24
        total += temp
    return total


print(sum_light([
datetime(2015, 1, 12, 10, 0, 0),
datetime(2015, 1, 12, 10, 0, 10),
datetime(2015, 1, 12, 11, 0, 0),
datetime(2015, 1, 13, 11, 0, 0)
]))



print((datetime(2015, 1, 12, 11, 0, 0)-datetime(2015, 1, 12, 11, 22, 0)).days)