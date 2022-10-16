# GitHub:
# https://github.com/sstankevych999/ekids226/blob/main/MyGame/flying_box.py
#
import pygame

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGTH = 600

YELLOW = (255, 255, 0)
MINT = (62, 180, 137)

GAME_WIN = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGTH))
pygame.display.set_caption("eKids - Flying box")
done = False
FPS = 60
clock = pygame.time.Clock()

rect_x = 100
rect_y = 100
rect_change_x = 5
rect_change_y = 3

while not done:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if rect_x > SCREEN_WIDHT - 50 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    if rect_y > SCREEN_HEIGTH - 50 or rect_y < 0:
        rect_change_y = rect_change_y * -1

    rect_x += rect_change_x
    rect_y += rect_change_y


    GAME_WIN.fill(MINT)
    pygame.draw.rect(GAME_WIN, YELLOW, (rect_x, rect_y, 50, 50), 0)