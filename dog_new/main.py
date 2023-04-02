import color
import stddraw
import random
import sys
import stdio
import stdarray

#вынести рисование белого квадрата с синей рамкой в отдельную функцию 

n = int(sys.argv[1])
x = y = n // 2
default_color = stddraw.BLUE
stddraw.setCanvasSize(500, 500)
stddraw.setXscale(0, n)
stddraw.setYscale(0, n)

a = stdarray.create2D(n, n, False)


def print_field():
    for i in range(0, n):
            for j in range(0, n):
                stddraw.setPenColor(stddraw.BLUE)
                stddraw.setPenRadius(0.001)
                stddraw.rectangle(i, j, 1, 1)


print_field()


def clear_field():
    stddraw.setPenRadius(0.001)
    for i in range(0, n):
        for j in range(0, n):
            if not a[i][j]:
                print_filled_square(i, j, stddraw.WHITE)
            else:
                print_filled_square(i, j, stddraw.GREEN)
            stddraw.rectangle(i, j, 1, 1)


def copy_field():
    global a
    a = stdarray.create2D(n, n, False)
    for i in range(0, n):
        for j in range(0, n):
            print_filled_square(i, j, stddraw.WHITE)
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.rectangle(i, j, 1, 1)


def print_filled_square(x, y, color):
    stddraw.setPenColor(color)
    stddraw.filledRectangle(x, y, 1, 1)
    stddraw.setPenColor(default_color)


def new_cords():
    new_x = random.randint(0, n - 1)
    new_y = random.randint(0, n - 1)
    while a[new_x][new_y]:
        new_x = random.randint(0, n - 1)
        new_y = random.randint(0, n - 1)

    return new_x, new_y


def evacuation(x_e, y_e, x, y):
    temp_x = x_e
    temp_y = y_e
    if temp_x > x:
        while temp_x > x:
            temp_x -= 0.1
            temp_y = (temp_x - x_e) * (y - y_e) / (x - x_e) + y_e
            stddraw.setPenColor(stddraw.RED)
            stddraw.setPenRadius(0.01)
            stddraw.point(temp_x, temp_y)
            stddraw.show(5)
            clear_field()

    else:
        while temp_x < x:
            temp_x += 0.1
            temp_y = (temp_x - x_e) * (y - y_e) / (x - x_e) + y_e
            stddraw.setPenColor(stddraw.RED)
            stddraw.setPenRadius(0.01)
            stddraw.point(temp_x, temp_y)
            stddraw.show(5)
            clear_field()

    stddraw.setPenRadius(0.001)
    stddraw.setPenColor(stddraw.BLUE)    

def evacuation_cords():
    r = random.randrange(1, 3)
    if r == 1:
        x_e = random.choice([0, n])
        y_e = random.choice([0, n])
    elif r == 2:
        x_e = random.choice([0, n])
        y_e = random.choice([0, n])

    return [x_e, y_e]


while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):

    if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
        a[x][y] = True
        print_filled_square(x, y, stddraw.GREEN)
        stddraw.rectangle(x, y, 1, 1)
        x_e, y_e = evacuation_cords()
        evacuation(x_e, y_e, x, y)
        x_old, y_old = x, y
        x, y = new_cords()
        evacuation(x_old, y_old, x, y)
        copy_field()
        continue

    a[x][y] = True
    print_filled_square(x, y, stddraw.GREEN)
    stddraw.rectangle(x, y, 1, 1)

    r = random.randrange(1, 5)
    if r == 1 and (not a[x+1][y]):
        x += 1
    elif r == 2 and (not a[x-1][y]):
        x -= 1
    elif r == 3 and (not a[x][y+1]):
        y += 1
    elif r == 4 and (not a[x][y-1]):
        y -= 1
    stddraw.show(100)
