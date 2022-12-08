import pygame


WIDTH = 1280
HEIGHT = 720
FRAMERATE = 200


def main():
    pygame.init()

    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('pygame-snake')
    clock = pygame.time.Clock()

    


if __name__ == '__main__':
    main()