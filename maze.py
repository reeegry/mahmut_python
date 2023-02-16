import colorama
from termcolor import colored
import random
from time import sleep
from os import system


colorama.init()

raw = int(input())
column = int(input())


def create_blocks(maze):
    for m in range(raw):
        for p in range(column):
            block = random.randint(0, 100)

            if 0 <= block <= 60:
                maze[m][p] = "X"


def print_maze(maze):
    for i in range(raw):
        print(maze[i])

    print("\n") 


def hero_get_pos(maze: list) -> list:
    i = random.randint(1, raw - 2)
    j = random.randint(1, column - 2)
    maze[i][j] = "*"

    return[i, j]

def end_indexes(maze):
    exits_list = []
    for i in range(column):
        if maze[0][i] == "0":
            exits_list.append([0, i])
        if maze[raw - 1][i] == "0":
            exits_list.append([raw - 1, i])
    
    for i in range(1, raw - 1):
        if maze[i][0] == "0":
            exits_list.append([i, 0])
        if maze[i][column - 1] == "0":
            exits_list.append([i, column - 1])

    return exits_list


def make_step(step):
    for i in range(raw):
        for j in range(column):
            if wave_list[i][j] == step:
                if i > 0 and wave_list[i - 1][j] == 0 and maze[i - 1][j] == "0":
                    wave_list[i - 1][j] = step + 1
                if j > 0 and wave_list[i][j - 1] == 0 and maze[i][j - 1] == "0":
                    wave_list[i][j - 1] = step + 1
                if i < raw - 1 and wave_list[i + 1][j] == 0 and maze[i + 1][j] == "0":
                    wave_list[i + 1][j] = step + 1
                if j < column - 1 and wave_list[i][j + 1] == 0 and maze[i][j + 1] == "0":
                    wave_list[i][j + 1] = step + 1


def create_matrix(m, n, default=0):
    matrix = [[default for i in range(n)] for j in range(m)]
    return matrix


def reached_the_end(end, w):
    for i in range(len(end) - 1):
        if w[end[i][0]][end[i][1]] != 0:
            return [end[i][0], end[i][1]]
    
    return [-1, -1]



wave_list = create_matrix(raw, column)
maze = create_matrix(raw, column, "0")
create_blocks(maze)
hero_cords = hero_get_pos(maze)
wave_list[hero_cords[0]][hero_cords[1]] = 1
end = end_indexes(maze)
k = 0
while True:
    k += 1
    make_step(k)
    if k > raw * column:
        k = 0
        wave_list = create_matrix(raw, column)
        maze = create_matrix(raw, column, "0")
        create_blocks(maze)
        hero_cords = hero_get_pos(maze)
        wave_list[hero_cords[0]][hero_cords[1]] = 1
        end = end_indexes(maze)
    
    if reached_the_end(end, wave_list) != [-1, -1]:
        i, j = reached_the_end(end, wave_list)
        break


i, j = reached_the_end(end, wave_list)
k = wave_list[i][j]
the_path = [(i, j)]
while k > 1:
    if i > 0 and wave_list[i - 1][j] == k - 1:
        i, j = i - 1, j
        the_path.append((i, j))
        k -= 1
    elif j > 0 and wave_list[i][j - 1] == k - 1:
        i, j = i, j - 1
        the_path.append((i, j))
        k -= 1
    elif i < raw and wave_list[i + 1][j] == k - 1:
        i, j = i + 1, j
        the_path.append((i ,j))
        k -= 1
    elif j < column and wave_list[i][j + 1] == k - 1:
        i, j = i, j + 1
        the_path.append((i, j))
        k -= 1

print_maze(maze)
for i in range(len(the_path) - 1, 0, -1):
    sleep(3)
    system("cls || clear")
    maze[the_path[i][0]][the_path[i][1]] = "0"
    maze[the_path[i - 1][0]][the_path[i - 1][1]] = "*"
    print_maze(maze)







