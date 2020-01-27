import sys
import pygame
from pygame.locals import QUIT

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

CLOCK = pygame.time.Clock()
FPS = 60

def main():
    score = 0
    scoreFont = pygame.font.SysFont(None, 36)

    while True:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        score_str = str(score).zfill(5)
        score_view = scoreFont.render(score_str, True, WHITE)
        SCREEN.blit(score_view, (400, 10))
        pygame.display.update()
        CLOCK.tick(FPS)

if __name__ == '__main__':
    main()