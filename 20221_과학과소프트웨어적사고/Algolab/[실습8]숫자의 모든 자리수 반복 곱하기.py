t = int(input())

while (t):
    n = str(input())
    
    while (int(n) > 9):
        sol = 1
        for i in n:
            if (i != '0'):
                sol *= int(i)
        n = str(sol)
        
    print(n)
    t -= 1
