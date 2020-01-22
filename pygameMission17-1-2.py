import pygame

pygame.init()

SCREEN = pygame.display.set_mode((300, 300))
pygame.display.set_caption("My Game")

def main():
    while True:
        SCREEN.fill((0, 0, 0))

if __name__ == '__main__':
    main()