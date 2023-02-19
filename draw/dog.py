import pygame
import random
import sys

WHITE = (255, 255, 255)
BLACK = (255, 0, 0)

pygame.init()
size = width, height = 400, 400

screen = pygame.display.set_mode(size)
screen.fill(WHITE)

n, trials = list(map(int, input().split()))
dead_ends = 0

def field_draw():
    GRID_W = width / n
    GRID_H = height / n

    for i in range(n + 2):
        pygame.draw.line(screen, BLACK, (GRID_W * i, 0), (GRID_W * i, height), 2)
        pygame.draw.line(screen, BLACK, (0, GRID_H * i), (width, GRID_H * i), 2) 

def dog_steps():
    a = [[False for _ in range(n)] for _ in range(n)]
    x = n // 2
    y = n // 2
    while (x > 0) and (x < n - 1) and (y > 0) and (y < n - 1):
        a[x][y] = True
        if a[x - 1][y] and a[x + 1][y] and a[x][y - 1] and a[x][y + 1]:
            dead_ends += 1
            break
        
        r = random.randrange(1, 5)
        if r == 1 and (not a[x + 1][y]): x += 1
        elif r == 2 and (not a[x - 1][y]): x -= 1
        elif r == 3 and (not a[x][y + 1]): y += 1
        elif r == 4 and (not a[x][y - 1]): y -= 1

t_count = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for t in range(trials):
        dog_steps()
        field_draw()
        pygame.display.flip()
        t_count += 1

    if t_count == trials:
        break
    

        


    print(str(100 * dead_ends // trials) + '% dead ends')