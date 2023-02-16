import pygame
import random
import sys


pygame.init()

screen = pygame.display.set_mode((400, 400))
r = pygame.Rect(50, 50, 100, 200)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

n, trials = list(map(int, input().split()))
dead_ends = 0

def field_draw():
    

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    #     for t in range(trials):
    #         a = [[False for _ in range(n)] for _ in range(n)]
    #         x = n // 2
    #         y = n // 2
    #         while (x > 0) and (x < n - 1) and (y > 0) and (y < n - 1):
    #             a[x][y] = True
    #             if a[x - 1][y] and a[x + 1][y] and a[x][y - 1] and a[x][y + 1]:
    #                 dead_ends += 1
    #                 break
                
    #             r = random.randrange(1, 5)
    #             if r == 1 and (not a[x + 1][y]): x += 1
    #             elif r == 2 and (not a[x - 1][y]): x -= 1
    #             elif r == 3 and (not a[x][y + 1]): y += 1
    #             elif r == 4 and (not a[x][y - 1]): y -= 1

    # print(str(100 * dead_ends // trials) + '% dead ends')