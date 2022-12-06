import random


m = int(input())
n = int(input())
bomb_amount = int(input())

field = [['0' for i in range(m + 2)] for i in range(n + 2)]

def bomb_cords():
    bomb_raw = random.randint(1, m)
    bomb_column = random.randint(1, n)

    return bomb_raw, bomb_column

for i in range(bomb_amount):
    bomb_raw, bomb_column = bomb_cords()

    while field[bomb_raw][bomb_column] == '*':  
        bomb_raw, bomb_column = bomb_cords()
    
    field[bomb_raw][bomb_column] = '*'

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if field[i][j] == '0':
            field[i][j] = str(sum([1 for m in range(-1, 2) for p in range(-1, 2) if field[i + m][j + p] == '*']))

for i in range(1, m + 1):
    for j in range(1, n + 1):
        print(field[i][j], end=' ')
    print()


