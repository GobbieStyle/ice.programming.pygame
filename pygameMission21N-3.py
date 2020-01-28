import sys
import pygame
import random
from pygame.locals import QUIT, Rect, KEYUP, KEYDOWN, K_LEFT, K_RIGHT

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

CLOCK = pygame.time.Clock()
FPS = 60

class Object:
    def draw(self):
        SCREEN.blit(self.image, Rect(self.x, self.y, self.width, self.height))


class Ship(Object):
    def __init__(self):
        self.image = pygame.image.load("ship.png")
        self.width = 30
        self.height = 30
        self.x = (SCREEN_WIDTH * 0.5) - (self.width * 0.5)
        self.y = SCREEN_HEIGHT * 0.9
        self.hp = 3

class Enemy(Object):
    def __init__(self):
        self.image = pygame.image.load("enemy.png")
        self.width = 30
        self.height = 30
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = 0
        self.speed = 4

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.move_init()

    def move_init(self):
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = 0
        self.speed += 2

def key_event(keymap, ship):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if not event.key in keymap:
                keymap.append(event.key)

        elif event.type == KEYUP:
            keymap.remove(event.key)

    if K_LEFT in keymap:
        ship.x -= 5
    if K_RIGHT in keymap:
        ship.x += 5

def main():
    ship = Ship()
    enemy = Enemy()
    keymap = []

    score = 0
    scoreFont = pygame.font.SysFont(None, 36)

    while True:
        SCREEN.fill(BLACK)

        ship.draw()
        enemy.draw()
        enemy.move()

        key_event(keymap, ship)

        score_str = str(score).zfill(5)
        score_view = scoreFont.render(score_str, True, WHITE)
        SCREEN.blit(score_view, (400, 10))
        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == '__main__':
    main()