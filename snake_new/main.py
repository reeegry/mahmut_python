import color
import stddraw
import random
import sys
import stdio
import stdarray


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

def print_apple():
    x = random.randint(2, n - 2)
    y = random.randint(2, n - 2)
    while a[x][y] == True:
        x = random.randint(2, n - 2)
        y = random.randint(2, n - 2)
        
    if a[x][y] == False:
        print_filled_square(x, y, stddraw.RED)

    return [x, y]

def print_cell(x, y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(x, y, 1, 1)
    stddraw.setPenColor(default_color)
    stddraw.rectangle(x, y, 1, 1)

def print_filled_square(x, y, color):
    stddraw.setPenColor(color)
    stddraw.filledRectangle(x, y, 1, 1)
    stddraw.setPenColor(default_color)

k_x = 0
k_y = 0

x_apple, y_apple = print_apple()
snake_cords_to_draw = [[x, y]]


while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):

    if stddraw.hasNextKeyTyped():
        direction = stddraw.nextKeyTyped()
        if direction == 'w' and k_y != -1:
            k_x = 0
            k_y = 1
        if direction == 's' and k_y != 1:
            k_x = 0
            k_y = -1
        if direction == 'a' and k_x != 1:
            k_x = -1
            k_y = 0
        if direction == 'd' and k_x != -1:
            k_x = 1
            k_y = 0

    x += k_x
    y += k_y

    if a[x][y] == True:
        break

    if k_x + k_y != 0:
        snake_cords_to_draw.append([x, y])
        a[x][y] = True

    for snake_x, snake_y in snake_cords_to_draw:
        print_filled_square(snake_x, snake_y, stddraw.GREEN)
    
    if len(snake_cords_to_draw) > 1:
        if not (x == x_apple and y == y_apple):
            old_x, old_y = snake_cords_to_draw[0]
            a[old_x][old_y] = False
            print_cell(old_x, old_y)
            snake_cords_to_draw = snake_cords_to_draw[1:]
        else:
            x_apple, y_apple = print_apple()

    stddraw.show(100)
