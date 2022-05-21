# 소프트웨어학부 20213009 서지훈
# 주가 분석(1)

t = int(input())

for i in range(0, t, 1):
    n = list(map(int, input().split()))
    left = n[1]
    now = n[2]
    right = n[3]
    count = 0

    for j in range(1, n-1, 1):
        if (now == right):
            right = n[i+3]
            continue