t = int(input())

while (t):
    n = str(input())
    len_ = len(n)
    sum_ = 0
    n = int(n)
    n_ = n

    while (n_):
        sum_ += ((n_ % 10) ** len_)
        n_ //= 10

    if(n == sum_):
        print(1)
    else:
        print(0)
    
    t -= 1
