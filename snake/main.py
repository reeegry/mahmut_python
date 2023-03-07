from pynput import keyboard
import random
import stddraw
import sys
import stdarray
import stdio
import pygame

import graphcom

pygame.init()

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


def print_apple():
    x = random.randint(2, n - 2)
    y = random.randint(2, n - 2)
    if a[x][y] == False:
        print_square(x, y, stddraw.RED)

    return [x, y]

print_field(n)

print_square(x, y, stddraw.GREEN)

k_x = 0
k_y = 0

x_apple, y_apple = print_apple()
snake_cords_to_draw = []
while (x > 0) and (x < n-1) and (y > 0) and (y < n-1):

    if stddraw.hasNextKeyTyped():
        direction = stddraw.nextKeyTyped()
        if direction == 'w':
            k_x = 0
            k_y = 1
        if direction == 's':
            k_x = 0
            k_y = -1
        if direction == 'a':
            k_x = -1
            k_y = 0
        if direction == 'd':
            k_x = 1
            k_y = 0

    x += k_x
    y += k_y

    if k_x + k_y != 0:
        snake_cords_to_draw.append([x, y])
        a[x][y] = True

    for snake_x, snake_y in snake_cords_to_draw:
        print_square(snake_x, snake_y, stddraw.GREEN)
    
    if len(snake_cords_to_draw) > 1:
        if not (x == x_apple and y == y_apple):
            old_x, old_y = snake_cords_to_draw[0]
            a[old_x][old_y] = False
            print_square(old_x, old_y, stddraw.BLUE)
            snake_cords_to_draw = snake_cords_to_draw[1:]
        else:
            x_apple, y_apple = print_apple()
    

    


    # a[x][y] = True
    # a[x - k_x][y - k_y] = False
    #print_square(x, y, stddraw.BLACK)

    # if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
    #     break


    # print_square(x - k_x, y - k_y, stddraw.BLUE)
    # print_square(x, y, stddraw.GREEN)



    

    stddraw.show(100)
    
    