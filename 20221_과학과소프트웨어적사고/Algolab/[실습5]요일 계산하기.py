def leap_year(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False
    

month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
t = int(input())

while (t):
    Y, M, D = map(int, input().split())
    day = 0

    for i in range(1, Y):
        if (leap_year(i)):
            day += 366
        else:
            day += 365

    for i in range(1, M):
        day += month[i]

    if (M > 2):
        if (leap_year(Y)):
            day += 1

    day += D

    print(day % 7)
    t -= 1
