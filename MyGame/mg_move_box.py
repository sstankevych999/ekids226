# GitHub:
# https://github.com/sstankevych999/ekids226/blob/main/MyGame/my_game.py
#
import pygame

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGTH = 600

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHT_YELLOW = (255, 255, 204)
MINT = (62, 180, 137)
BROWN = (150, 75, 0)
GOLD = (255, 204, 0)
box_color = BLUE

GAME_WIN = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGTH))
pygame.display.set_caption("eKids Game")
done = False
FPS = 60
clock = pygame.time.Clock()

bg_sound = pygame.mixer.Sound("game_bg_sound.wav")
bg_sound.play()

rect_x = 0
rect_y = 0
rect_width = 50
rect_height = 50
rect_change_x = 5
rect_change_y = 3

while not done:
    clock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_x > SCREEN_WIDHT-rect_width or rect_x < 0:
        rect_change_x *= -1
        box_color = BROWN
    if rect_y > SCREEN_HEIGTH-rect_height or rect_y < 0:
        rect_change_y *= -1
        box_color = BLUE
    if rect_x == 0 and rect_y == SCREEN_HEIGTH:
        box_color = GOLD

    GAME_WIN.fill(WHITE)
    pygame.draw.rect(GAME_WIN, box_color, (rect_x, rect_y, rect_width, rect_height), 0)

