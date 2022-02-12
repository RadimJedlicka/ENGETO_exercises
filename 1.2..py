def num_days(date1, date2):

    days = 0

    if date1 > date2:
        days = -1
    else:
        while date1 < date2:
            date1 = increase(date1)
            days += 1

    return days


def increase(date):

    y,m,d = date
    # february
    if m == 2 and d in [28,29]:
        if is_leap(y) and d == 28:
            date =(y,m,d+1)
        else:
            date =(y,m+1,1)

    # month end
    elif (m in [1,3,5,7,8,10] and d == 31) \
        or (m in [4,6,9,11] and d == 30):
        date =(y,m+1,1)
    # year end
    elif m == 12 and d == 31:
        date = (y+1,1,1)
    #in month
    else:
        date = (y,m,d+1)

    return date


def is_leap(y):
    result = False

    if y % 400 == 0 \
        or (y % 4 == 0 and y % 100 != 0):
        result = True

    return result


if __name__=='__main__':
    import pdb; pdb.set_trace()

    date1 = (2013,1,1)
    date2 = (2017,1,1)
    num_days(date1, date2)