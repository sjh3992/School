t = int(input())

while (t):
    a, b, c = map(int, input().split())
    
    if (a <= b):
        if (b <= c):
            print(a, b, c)
        elif (a <= c):
            print(a, c, b)
        else:
            print(c, a, b)
    elif (c <= b):
        print(c, b, a)
    elif(a <= c):
        print(b, a, c)
    else:
        print(b, c, a)
        
    t -= 1
