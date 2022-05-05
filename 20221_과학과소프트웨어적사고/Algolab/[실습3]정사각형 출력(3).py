t = int(input())

while (t):
    n = int(input())

    for i in range(0, n):
        for j in range(0, n):
            if (i == 0 or i == n//2 or i == n-1):
                if(j == 0 or j == n//2 or j == n-1):
                    if(i == j and j == n//2):
                        print("*", end="")
                    else:
                        print("+", end="")
                else:
                    print("-", end="")

            elif (j == 0 or j == n//2 or j == n-1):
                print("|", end="")
            
            elif (i == j):
                print("\\", end="")

            elif (i == n-j-1):
                print("/", end="")

            else:
                print(".", end="")

        print("")
    t -= 1
