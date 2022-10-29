# GitHub:
# https://github.com/sstankevych999/ekids226/blob/main/MyGame/my_game.py
#
import pygame

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGTH = 600

YELLOW = (255, 255, 0)
MINT = (62, 180, 137)
BROWN = (150, 75, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        width = 40
        heigth = 60
        self.image = pygame.Surface( (width, heigth) )
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def jump(self):
        self.rect.y += 2
        if self.rect.bottom >= SCREEN_HEIGTH:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0
        self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.35

        if self.rect.y >= SCREEN_HEIGTH - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGTH - self.rect.height

    def update(self):
         self.calc_grav()
         self.rect.x += self.change_x
         self.rect.y += self.change_y

# bg_sound = pygame.mixer.Sound("game_bg_sound.wav")
# bg_sound.play()

GAME_WIN = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGTH))
pygame.display.set_caption("eKids Game")
done = False
FPS = 60
clock = pygame.time.Clock()

player = Player()
player.rect.x = (SCREEN_WIDHT-player.rect.width)/2
player.rect.y = SCREEN_HEIGTH - player.rect.height

active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(player)


while not done:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_UP:
                player.jump()

        elif event.type == pygame.KEYUP:
            player.stop()

    active_sprite_list.update()
    GAME_WIN.fill(MINT)
    active_sprite_list.draw(GAME_WIN)



