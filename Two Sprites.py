import pygame
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_CAPTION = "Sprite Movement Game"
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_COLOR = RED
PLAYER_SPEED = 5
OTHER_WIDTH = 70
OTHER_HEIGHT = 70
OTHER_COLOR = BLUE
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, initial_x, initial_y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = initial_x
        self.rect.y = initial_y
        self.speed = PLAYER_SPEED
    def move_up(self):
        self.rect.y -= self.speed
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.y += self.speed
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

class OtherSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
player_start_x = 50
player_start_y = WINDOW_HEIGHT // 2 - PLAYER_HEIGHT // 2
player = Player(PLAYER_COLOR, PLAYER_WIDTH, PLAYER_HEIGHT, player_start_x, player_start_y)
other_sprite_x = WINDOW_WIDTH - OTHER_WIDTH - 100
other_sprite_y = WINDOW_HEIGHT // 2 - OTHER_HEIGHT // 2
other_sprite = OtherSprite(OTHER_COLOR, OTHER_WIDTH, OTHER_HEIGHT, other_sprite_x, other_sprite_y)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
all_sprites_list.add(other_sprite)
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move_right()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move_up()
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move_down()
    screen.fill(GREEN)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()