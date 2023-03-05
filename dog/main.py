import random
import stddraw
import sys
import stdarray
import stdio

import graphcom

n = int(input("Размер поля "))

a = stdarray.create2D(n, n, False)
x = n // 2
y = n // 2


def print_square(x, y, color):
    stddraw.setPenColor(color)
    stddraw.square(x / (n - 1), y / (n - 1), 1 / (3 * (n - 1)) )


def print_field(n):
    for i in range(0, n):
        for j in range(0, n):
            print_square(i, j, stddraw.BLUE)

print_field(n)

print_square(x, y, stddraw.GREEN)
while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):
    a[x][y] = True
    # Проверить туnик и сделать случайный ход .
    print_square(x, y, stddraw.BLACK)
    if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
        #Эвакуация
        x1 = x
        y1 = y
        while a[x1][y1]:
            x1 = random.randrange(0, n)
            y1 = random.randrange(0, n)
        stX = random.randint(1, 4)
        if stX == 1:
            stX = 0
            stY = random.randrange(0, n)
        elif stX == 2:
            stX = n-1
            stY = random.randrange(0, n)
        elif stX == 3:
            stX = random.randrange(0, n)
            stY = 0
        else:
            stX = random.randrange(0, n)
            stY = n-1
        graphcom.roadTo(stX, stY, x, y, n)
        graphcom.roadTo(x, y, x1, y1, n)

        x = x1
        y = y1
        continue

    r = random.randrange(1, 5)
    if r == 1 and (not a[x+1][y]):
        x += 1
    elif r == 2 and (not a[x-1][y]):
        x -= 1
    elif r == 3 and (not a[x][y+1]):
        y += 1
    elif r == 4 and (not a[x][y-1]):
        y -= 1
    print_square(x, y, stddraw.GREEN)
    stddraw.show(100)