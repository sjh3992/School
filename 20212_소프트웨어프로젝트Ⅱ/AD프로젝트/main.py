import pygame, random, sys
from block_data import block_data, color
from field import field, shape, bottom
from field import field_init, shapeNow

def drawing():
    screen.fill([0, 0, 0])
    for i in range(0, 25, 1):
        for j in range(0, 12, 1):
            pygame.draw.rect(screen, color[field[i][j]], [20*(j+1), 20*(i+1), 19, 19])
    pygame.display.flip()

def collision_test():
    for x in bottom:
        if field[x[0]+1][x[1]] != 0:
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
    drawing()
    print(shape)
    for i in range(0, 25):
        print(field[i])

def debugging():
    for i in range(0, 25, 1):
        print(field[i])
    print()

# initialize engine
pygame.init()

# set screen
size = [380, 540]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("테트리스 게임")

# init
field_init()
now_shape = random.randrange(1, 8)
shapeNow(now_shape)
next_shape = random.randrange(1, 8)

# loop
clock = pygame.time.Clock()
pressed = None

while True:
    # frame per seconds
    clock.tick(1)

    # main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
        

    # block
    if collision_test() == True:
        now_shape = next_shape
        shapeNow(now_shape)
        next_shape = random.randrange(1, 8)
    else:
        down()
            
    # drawing
    #drawing()
