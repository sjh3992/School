from block_data import block_data

field = []
shape = []
bottom = []

def field_init():
    for i in range(0, 4, 1):
        field.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(4, 24, 1):
        field.append([8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8])
    field.append([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8])


def shapeNow(num):
    print("now shape:", num)
    
    for i in range(0, 4, 1):
        for j in range(4, 8, 1):
            field[i][j] = 0
    
    if num == 1:
        field[2][5] = block_data[1][0][0]
        field[2][6] = block_data[1][0][1]
        field[3][5] = block_data[1][0][2]
        field[3][6] = block_data[1][0][3]
        shape = [[2, 5], [2, 6], [3, 5], [3, 6]]
        bottom = [[3, 5], [3, 6]]

    elif num == 7:
        s = 0
        for i in range(0, 4, 1):
            for j in range(4, 8, 1):
                field[i][j] = block_data[7][0][s]
                s += 1
                shape = [[3, 4], [3, 5], [3, 6], [3, 7]]
                bottom = [[3, 4], [3, 5], [3, 6], [3, 7]]

    else:
        s = 0
        for i in range(1, 4, 1):
            for j in range(4, 7, 1):
                field[i][j] = block_data[num][0][s]
                s += 1
                if field[i][j] != 0:
                    shape.append([i, j])
        for j in range(4, 7, 1):
            if field[3][j] != 0:
                bottom.append([3, j])

    print("shape:", shape)
