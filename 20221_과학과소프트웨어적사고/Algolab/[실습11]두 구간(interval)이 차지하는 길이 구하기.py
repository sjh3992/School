t = int(input())

while t:
    a, b, c, d = map(int, input().split())
    overlapped = 0
    
    if (b <= c or d <= a):
        overlapped = 0
    elif (a <= c < b <= d):
        overlapped = b - c
    elif (a <= c < d <= b):
        overlapped = d - c
    elif (c <= a < b <= d):
        overlapped = b - a
    else:
        overlapped = d - a

    print(overlapped, b - a + d - c - overlapped)
    t -= 1
