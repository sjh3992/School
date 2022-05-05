t = int(input())

while (t):
    H, M = map(int, input().split())
    angle = int(abs((60 * H) - (11 * M)))
    if (angle >= 360):
        angle = 720 - angle

    print(angle // 2)
    t -= 1
