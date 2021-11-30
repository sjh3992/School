import pygame, random, sys
from block_data import block_data, color

field = list()
shape = list()
score = 0
rotation = 0

def field_init():
    for i in range(0, 4, 1):
        field.append([9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9])
    for i in range(4, 24, 1):
        field.append([8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
    field.append([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])

def drawing():
    screen.fill([0, 0, 0])
    for i in range(0, 25, 1):
        for j in range(0, 12, 1):
            pygame.draw.rect(screen, color[field[i][j]], [20*(j+1), 20*(i+1), 19, 19])
    name_text = [font.render("20213009", True, (255, 255, 255))]
    name_text.append(font.render("서지훈", True, (255, 255, 255)))
    score_text = font.render("점수 : " + str(score), True, (255, 255, 255))
    next_text = font.render("다음 도형", True, (255, 255, 255))
    screen.blit(score_text, (280, 100))
    screen.blit(next_text, (280, 140))
    screen.blit(name_text[0], (280, 40))
    screen.blit(name_text[1], (280, 60))
    pygame.display.flip()

def collision_test():
    if shape == []:
        return True
    for x in shape:
        if field[x[0]+1][x[1]] == 8 or field[x[0]+1][x[1]] == 10:
            #print("collision")
            return True
    #print("not collision")
    return False

def line_test():
    global score
    flag = True
    for i in range(23, 3, -1):
        for j in range(1, 11, 1):
            if field[i][j] != 10:
                flag = False
                break
        if flag == True:
            tetris(i)
            score += 100

def end_test():
    for i in range(0, 4, 1):
        for j in range(1, 11, 1):
            if field[i][j] != 0:
                return True
    return False

def collision():
    for x in shape:
        field[x[0]][x[1]] = 10

def tetris(num):
    for i in range(1, 11, 1):
        field[num][i] = 0
    for i in range(num-1, 3, -1):
        for j in range(1, 11, 1):
            field[i+1][j] = field[i][j]

def down():
    #print("down")
    for x in shape:
        field[x[0]][x[1]] = 0
    for i in range(0, len(shape), 1):
        shape[i][0] += 1
    for x in shape:
        field[x[0]][x[1]] = now_shape

def left():
    #print("left")
    for i in range(0, len(shape), 1):
        if shape[i][1] <= 1:
            return
    for x in shape:
        field[x[0]][x[1]] = 0
    for i in range(0, len(shape), 1):
        shape[i][1] -= 1
    for x in shape:
        field[x[0]][x[1]] = color[now_shape]
    
def right():
    #print("right")
    for i in range(0, len(shape), 1):
        if shape[i][1] >= 10:
            return
    for x in shape:
        field[x[0]][x[1]] = 0
    for i in range(0, len(shape), 1):
        shape[i][1] += 1
    for x in shape:
        field[x[0]][x[1]] = color[now_shape]

def rotate():
    global rotation
    if now_shape != 1:
        print("rotate")
        rotation += 1
        for x in shape:
            field[x[0]][x[1]] = 0
            
        shapeNow()

def game_end():
    end_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(end_text, (280, 500))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def shapeNow():
    global shape, rotation
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
        s = 0
        for i in range(0, 4, 1):
            for j in range(4, 8, 1):
                field[i][j] = block_data[7][rotation % 4][s]
                s += 1
                if field[i][j] != 0:
                    shape.append([i, j])
    else:
        s = 0
        for i in range(1, 4, 1):
            for j in range(4, 7, 1):
                field[i][j] = block_data[now_shape][rotation % 4][s]
                s += 1
                if field[i][j] != 0:
                    shape.append([i, j])

    print("shape:", shape)


# initialize engine
pygame.init()
field_init()
font = pygame.font.Font('부산바다체.ttf', 20)

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
                left()
            elif event.key == pygame.K_RIGHT:
                right()
            elif event.key == pygame.K_DOWN:
                down()
            elif event.key == pygame.K_SPACE:
                while not collision_test():
                    down()
            elif event.key == pygame.K_r:
                rotate()

    if collision_test() == True:
        if end_test() == True:
            game_end()
        collision()
        now_shape = random.randrange(1, 8)
        shapeNow()
        drawing()
    else:
        down()
        drawing()
        
    line_test()
