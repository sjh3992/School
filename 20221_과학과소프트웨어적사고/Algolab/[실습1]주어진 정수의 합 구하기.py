t = int(input())

for i in range(0, t):
    n = int(input())
    num = list(map(int, input().split()))
    sum_ = 0
    for j in range(0, n):
        sum_ += num[j]
    print(sum_)
