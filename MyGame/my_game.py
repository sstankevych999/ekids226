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



GAME_WIN = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGTH))
pygame.display.set_caption("eKids Game")
done = False
FPS = 60
clock = pygame.time.Clock()

cord_x = 400
cord_y = 300
speed_x = 0
speed_y = 0

while not done:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_x = -5
        elif event.type == pygame.KEYUP:
            speed_x = 0
            speed_y = 0


    cord_x = cord_x + speed_x
    cord_y = cord_y + speed_y

    GAME_WIN.fill(MINT)
    pygame.draw.circle(GAME_WIN, BLUE, (cord_x, cord_y), 25, 0)

# -------------------- Homework --------------------
# to finish suporting object movement with arrow keys
# завершити підтримку руку обєкту кнопками напрямків /стрілочками