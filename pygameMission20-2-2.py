import sys
import pygame
import random
from pygame.locals import QUIT, Rect

pygame.init()

# ------------------------------------ #

class Enemy:
    def __init__(self):
        self.image = pygame.image.load("enemy.png")
        self.width = 30
        self.height = 30
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = 0
        self.speed = 4

    def draw(self):
        SCREEN.blit(self.image, Rect(self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.move_init()

    def move_init(self):
        self.x = random.randrange(0, SCREEN_WIDTH - self.width)
        self.y = 0
        self.speed += 2

# ------------------------------------ #

BLACK = (0, 0, 0)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

CLOCK = pygame.time.Clock()
FPS = 60

def main():
    enemy = Enemy()

    while True:
        SCREEN.fill(BLACK)

        enemy.draw()
        enemy.move()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == '__main__':
    main()