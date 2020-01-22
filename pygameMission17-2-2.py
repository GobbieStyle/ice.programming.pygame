import sys
import pygame
from pygame.locals import QUIT

pygame.init()

BLACK = (0, 0, 0)

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

CLOCK = pygame.time.Clock()
FPS = 60

def main():
    while True:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == '__main__':
    main()