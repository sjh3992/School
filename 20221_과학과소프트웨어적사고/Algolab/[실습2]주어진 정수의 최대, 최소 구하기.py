t = int(input())

for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    max_, min_ = num[0], num[0]
    for j in range(1, n):
        if num[j] > max_:
            max_ = num[j]
        elif num[j] < min_:
            min_ = num[j]
    print(max_, min_)
