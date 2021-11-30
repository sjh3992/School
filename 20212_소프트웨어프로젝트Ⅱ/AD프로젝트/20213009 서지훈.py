import pygame, random, sys
from block_data import block_data, color

field = []
shape = []
score = 0
pressed = None


def debugging():
    for x in field:
        print(x)
    print(shape)
    print()

def field_init():
    for i in range(0, 4, 1):
        field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(4, 24, 1):
        field.append([8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
    field.append([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])

def drawing():
    screen.fill([0, 0, 0])
    for i in range(0, 25, 1):
        for j in range(0, 12, 1):
            pygame.draw.rect(screen, color[int(field[i][j])], [20*(j+1), 20*(i+1), 19, 19])
    score_text = font.render("점수 : " + str(score), True, (255, 255, 255))
    next_text = font.render("다음 도형", True, (255, 255, 255))
    screen.blit(score_text, (280, 100))
    screen.blit(next_text, (280, 140))
    pygame.display.flip()
    debugging()

def collision_test():
    if shape == []:
        return True
    for x in shape:
        if field[x[0]+1][x[1]] != 0 and field[x[0]+1][x[1]] != now_shape:
            print("collision")
            collision()
            return True
    print("not collision")
    return False

def end_test():
    for i in range(0, 4, 1):
        for j in range(1, 11, 1):
            if field[i][j] != 0:
                return True
    return False

def clear_test():
    for i in range(23, 3, -1):
        test = 0
        for j in range(1, 11, 1):
            if field[i][j] == 0:
                test = 0
                break
            test = 1
        if test == 1:
            score += 100
            for i in range(1, 11, 1):
                field[i][j] = 0
            for j in range(i, 3, -1):
                field[i][j] = field[i-1][j]

def collision():
    for i in range(0, 24, 1):
        for j in range(1, 11, 1):
            if field[i][j] != 0 and field[i][j] != 8:
                if field[i][j] == 1:
                    field[i][j] = 11
                elif field[i][j] == 2:
                    field[i][j] = 12
                elif field[i][j] == 3:
                    field[i][j] = 13
                elif field[i][j] == 4:
                    field[i][j] = 14
                elif field[i][j] == 5:
                    field[i][j] = 15
                elif field[i][j] == 6:
                    field[i][j] = 16
                else:
                    field[i][j] = 17

def down():
    print("down")
    for x in shape:
        field[x[0]][x[1]] = 0
    for i in range(0, len(shape), 1):
        shape[i][0] += 1
    for x in shape:
        field[x[0]][x[1]] = now_shape

def game_end():
    print("end")
    end_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(end_text, (280, 500))
    pygame.display.flip()

def left():
    for i in range(0, len(shape), 1):
        if shape[i][1] > 1:
            pass
        else:
            return
    for x in shape:
        field[x[0]][x[1]] = 0
    for i in range(0, len(shape), 1):
        shape[i][1] -= 1
    for x in shape:
        field[x[0]][x[1]] = color[now_shape]

def right():
    for i in range(0, len(shape), 1):
        if shape[i][1] < 10:
            pass
        else:
            return
    for x in shape:
        field[x[0]][x[1]] = 0
    for i in range(0, len(shape), 1):
        shape[i][1] += 1
    for x in shape:
        field[x[0]][x[1]] = color[now_shape]

def shapeNow():
    global shape
    shape.clear()
    
    print("now shape:", now_shape)
    
    for i in range(0, 4, 1):
        for j in range(4, 8, 1):
            field[i][j] = 0
    
    if now_shape == 1:
        field[2][5] = 1
        field[2][6] = 1
        field[3][5] = 1
        field[3][6] = 1
        shape = [[2, 5], [2, 6], [3, 5], [3, 6]]

    elif now_shape == 7:
        field[3][4] = 7
        field[3][5] = 7
        field[3][6] = 7
        field[3][7] = 7
        shape = [[3, 4], [3, 5], [3, 6], [3, 7]]

    else:
        s = 0
        for i in range(1, 4, 1):
            for j in range(4, 7, 1):
                field[i][j] = block_data[now_shape][0][s]
                s += 1
                if field[i][j] != 0:
                    shape.append([i, j])

    print("shape:", shape)

'''
def shapeNext():
    print("next shape:", next_shape)

    if next_shape == 1:
        pygame.draw.rect(screen, color[1], [280, 160, 19, 19])
        pygame.draw.rect(screen, color[1], [300, 160, 19, 19])
        pygame.draw.rect(screen, color[1], [280, 180, 19, 19])
        pygame.draw.rect(screen, color[1], [300, 180, 19, 19])

    elif next_shape == 7:
        pygame.draw.rect(screen, color[1], [280, 160, 19, 19])
        pygame.draw.rect(screen, color[1], [300, 160, 19, 19])
        pygame.draw.rect(screen, color[1], [320, 160, 19, 19])
        pygame.draw.rect(screen, color[1], [340, 160, 19, 19])

    else:
        for i in range(1, 3, 1):
            for j in range(0, 3, 1):
                if block_data[next_shape][0][3*i+j] != 0:
                    pygame.draw.rect(screen, color[next_shape], [260+20*i, 160+20*j, 19, 19])
'''

# initialize engine
pygame.init()
field_init()
font = pygame.font.Font('부산바다체.ttf', 20)
next_shape = random.randrange(1, 8)

# set screen
size = (400, 540)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("테트리스 게임")

# loop
clock = pygame.time.Clock()

while True:
    # frame
    clock.tick(1)

    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                left()
            elif event.key == pygame.K_RIGHT:
                print("right")
                right()
            elif event.key == pygame.K_r:
                rotate()
            elif event.key == pygame.K_DOWN:
                down()
            elif event.key == pygame.K_SPACE:
                while not collision_test():
                    down()
                    

    if collision_test() == True:
        if end_test() == True:
            game_end()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        else:
            now_shape = next_shape
            next_shape = random.randrange(1, 8)
            shapeNow()
            #shapeNext()
            drawing()
    else:
        down()
        drawing()
    
    clear_test()
    drawing()
