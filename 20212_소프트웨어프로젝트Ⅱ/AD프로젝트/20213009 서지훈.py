import pygame, random, sys
from block_data import block_data, color

field = []
shape = []
pressed = None

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
            pygame.draw.rect(screen, color[field[i][j]], [20*(j+1), 20*(i+1), 19, 19])
    pygame.display.flip()

def collision_test():
    if shape == []:
        return True
    for x in shape:
        if field[x[0]+1][x[1]] != 0 and field[x[0]+1][x[1]] != now_shape:
            print("collision")
            return True
        
    print("not collision")
    return False

def down():
    print("down")
    for x in shape:
        field[x[0]][x[1]] = 0
    for i in range(0, len(shape), 1):
        shape[i][0] += 1
    for x in shape:
        field[x[0]][x[1]] = now_shape
    

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


# initialize engine
pygame.init()
field_init()

# set screen
size = (380, 540)
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
            pressed = pygame.key.get_pressed()

    if collision_test() == True:
        now_shape = random.randrange(1, 8)
        shapeNow()
        drawing()
    else:
        down()
        drawing()

    '''
    # block
    if collision_test() == True:
        now_shape = next_shape
        shapeNow()
        next_shape = random.randrange(1, 8)
    else:
        down()

'''
