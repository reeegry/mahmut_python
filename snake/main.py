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
    while a[x][y] == True:
        x = random.randint(2, n - 2)
        y = random.randint(2, n - 2)
        
    if a[x][y] == False:
        print_square(x, y, stddraw.RED)

    return [x, y]

print_field(n)

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
        print_square(snake_x, snake_y, stddraw.GREEN)
    
    if len(snake_cords_to_draw) > 1:
        if not (x == x_apple and y == y_apple):
            old_x, old_y = snake_cords_to_draw[0]
            a[old_x][old_y] = False
            print_square(old_x, old_y, stddraw.BLUE)
            snake_cords_to_draw = snake_cords_to_draw[1:]
        else:
            x_apple, y_apple = print_apple()
    

    stddraw.show(100)
    
    