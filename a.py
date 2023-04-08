import pygame
import sys
import random
import time
import heapq
from math import sqrt

n = int(input())
m = int(input())
# a = [['0' for i in range(m)] for _ in range(n)]

# for i in range(n):
#     for j in range(m):
#         r = random.random()
#         a[i][j] = 'X' if r < 0.3 else '0'

SCREEN_COLOR = (100, 150, 200)
WHITE = (0, 0, 0)
GRAY = (105, 105, 105)
ORANGE = (255,69,0)
GREEN = (51, 255, 51)
SQUARE_SIZE = 12
HEIGHT = SQUARE_SIZE * n
LENGTH = SQUARE_SIZE * m

pygame.init()
canvas = pygame.display.set_mode((HEIGHT, LENGTH))
canvas_rect = canvas.get_rect()
canvas.fill(SCREEN_COLOR)


def print_field():
    for i in range(n + 1):
        pygame.draw.line(canvas, WHITE, [0, i * SQUARE_SIZE], [LENGTH, i * SQUARE_SIZE])   

    for i in range(m + 1):
        pygame.draw.line(canvas, WHITE, [i * SQUARE_SIZE, 0], [i * SQUARE_SIZE, HEIGHT])      

    pygame.display.update()

print_field()


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]


class Node:
    def __init__(self, cords, cost):
        self.x, self.y = cords
        self.node_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.node_rect = self.node_surface.get_rect(topleft=cords)
        self.cost = cost
        self.g = 0
        
    
    def h(self, end_cords):
        x_end, y_end = end_cords
        return abs(self.x - x_end) + abs(self.y - y_end)

    def f(self, start_cords, end_cords):
        return self.h(end_cords) + self.g(start_cords)
    
    def fill_square(self, color=SCREEN_COLOR):
        self.node_surface.fill(color)
        canvas.blit(self.node_surface, self.node_rect)
        print_field()


class Grid:
    def __init__(self):
        self.a = [['0' for i in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                r = random.random()
                self.a[i][j] = 'X' if r < 0.3 else '0'
        
        self.create_nodes()
    
    def create_nodes(self):
        self.vertexes = [[None for _ in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if self.a[i][j] == '0':
                    node = Node((i * SQUARE_SIZE, j * SQUARE_SIZE), 1)
                    node.fill_square()
                else:
                    node = Node((i * SQUARE_SIZE, j * SQUARE_SIZE), 0)
                    node.fill_square(GRAY)

                self.vertexes[i][j] = node
    
    def neighbors(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        return results

grid = Grid()

def waypoint(color):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    if not grid.a[x // SQUARE_SIZE][y // SQUARE_SIZE] == 'X':
                        square_pressed = grid.vertexes[x // SQUARE_SIZE][y // SQUARE_SIZE]
                        square_pressed.fill_square(color)
                        pygame.display.update()

                        return (x // SQUARE_SIZE, y // SQUARE_SIZE)


start = waypoint(ORANGE)
stop = waypoint(GREEN)


def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in grid.neighbors(current):
            print(next)
            if 0 <= next[0] < m and 0 <= next[1] < n:
                if grid.a[next[0]][next[1]] == '0':
                    new_cost = cost_so_far[current] + 1
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        priority = new_cost + grid.vertexes[next[0]][next[1]].h(goal)
                        frontier.put(next, priority)
                        came_from[next] = current
    
    return came_from, cost_so_far

came_from, cost_so_far = a_star_search(grid, start, stop)
# print(came_from, cost_so_far)

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    
    return path

path = reconstruct_path(came_from, start, stop)
print(path)

for i, j in path[::-1]:
    grid.vertexes[i][j].fill_square(ORANGE)
    grid.vertexes[stop[0]][stop[1]].fill_square(GREEN)
    time.sleep(0.1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


