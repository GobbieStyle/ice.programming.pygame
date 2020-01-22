import sys
import pygame
from pygame.locals import QUIT

pygame.init()

SCREEN = pygame.display.set_mode((300, 300))
pygame.display.set_caption("My Game")

def main():
    while True:
        SCREEN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()