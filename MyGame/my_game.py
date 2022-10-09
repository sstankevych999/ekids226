import pygame

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGTH = 600

GAME_WIN = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGTH))
pygame.display.set_caption("eKids Game")
done = False
FPS = 60
clock = pygame.time.Clock()

while not done:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    YELLOW = (255, 255, 0)
    pygame.draw.rect(GAME_WIN, YELLOW, (0,0,100,100), 0)