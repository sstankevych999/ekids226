import pygame
from random import randrange

pygame.init()

SCREEN_WIDHT = 800
SCREEN_HEIGTH = 600

BG_IMAGE = pygame.image.load("arctic_background.jpg")
PLATFORM_IMAGE = pygame.image.load("cloud_platform.png")
PlAYER_IMAGE = pygame.image.load("tux40x60alpha.png")

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
        self.image = PlAYER_IMAGE.convert_alpha()
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        self.rect.y -= 2
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGTH:
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
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
             self.rect.right = block.rect.left
            elif self.change_x < 0:
             self.rect.x = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(BROWN)
        self.image = PLATFORM_IMAGE
        self.rect = self.image.get_rect()

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        w , h = 30, 30
        self.image = pygame.Surface([w, h])
        self.image.fill(YELLOW)
        # self.image = PLATFORM_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
platform_list = pygame.sprite.Group()

platforms = [
    [210,70, 500,500],
    [210,70, 200,400],
    [210,70, 600,300],
    [210,70, 180,200]
]
for platform in platforms:
    block = Platform(platform[0], platform[1])
    block.rect.x = platform[2]
    block.rect.y = platform[3]
    platform_list.add(block)

coin_list = pygame.sprite.Group()

def mine_coin(coin_list, platforms):
    random_place = randrange( len(platforms))
    pos = platforms[random_place]
    x = pos[2] + randrange(pos[0])
    y = pos[3] - 100
    coin = Coin(x, y)
    coin_list.add(coin)

mine_coin(coin_list, platforms)
main_font = pygame.font.SysFont("comicsans", 50)
coin_count = 0

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

    hits = pygame.sprite.spritecollide(player, coin_list, False)
    if hits:
        coin_count += 1
        coin_list.remove(hits)
        mine_coin(coin_list, platforms)

    # GAME_WIN.fill(MINT)
    GAME_WIN.blit(BG_IMAGE, (0, 0))
    coin_label = main_font.render(f"Coins: {coin_count}", 1, BROWN)
    GAME_WIN.blit(coin_label, (10, 10))
    platform_list.draw(GAME_WIN)
    coin_list.draw(GAME_WIN)
    active_sprite_list.draw(GAME_WIN)



