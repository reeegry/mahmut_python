import pygame

game_active = True

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("gklj")


k = 0
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        k = 1
       
    screen.fill((200, 200, 200))
    pygame.display.flip()
    print(k)