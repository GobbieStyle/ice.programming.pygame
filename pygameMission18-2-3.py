import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

CLOCK = pygame.time.Clock()
FPS = 60

class Ship:
    def __init__(self):
        self.image = pygame.image.load("Ship.png")
        self.width = 30
        self.height = 30
        self.x = SCREEN_WIDTH * 0.5 - self.width * 0.5
        self.y = SCREEN_HEIGHT * 0.9
        self.hp = 3

    def draw(self):
        SCREEN.blit(self.image, Rect(self.x, self.y, self.width, self.height))

def main():
    ship = Ship()

    score = 0
    scoreFont = pygame.font.SysFont(None, 36)
    while True:
        SCREEN.fill(BLACK)

        ship.draw()

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