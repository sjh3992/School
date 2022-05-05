# 두사각형면적둘레구하기
# 소프트웨어학부 20213009 서지훈

def overlap(a, b, c, d):
    if (b <= c or d <= a):
        return 0
    elif (a <= c < b <= d):
        return b - c
    elif (a <= c < d <= b):
        return d - c
    elif (c <= a < b <= d):
        return b - a
    else:
        return d - a

t = int(input())

while t:
    p1x, p1y, q1x, q1y, p2x, p2y, q2x, q2y = map(int, input().split())

    x_overlapped = overlap(p1x, q1x, p2x, q2x)
    y_overlapped = overlap(p1y, q1y, p2y, q2y)

    area = (q1x - p1x) * (q1y - p1y) + (q2x - p2x) * (q2y - p2y)
    length = ( (q1x - p1x) + (q1y - p1y) + (q2x - p2x) + (q2y - p2y) ) * 2

    if (x_overlapped == 0 or y_overlapped == 0):
        print(area, length)
    else:
        print(area - x_overlapped * y_overlapped, length - (x_overlapped + y_overlapped) * 2)
    
    t -= 1
