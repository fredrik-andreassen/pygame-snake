import pygame
import sys

from Board import Board


WIDTH = 1280
HEIGHT = 720

if len(sys.argv) >= 2 and sys.argv[1] == 'debug':
    MODE = 'debug'
    try:
        FRAMERATE = int(sys.argv[2])
    except:
        FRAMERATE = 10
else:
    MODE = 'normal'
    FRAMERATE = 200

STEP = 20

def main():
    pygame.init()

    main_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('pygame-snake')
    clock = pygame.time.Clock()

    board = Board(main_surface, STEP)
    board.add_snake({pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left'})

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            
            if event.type == pygame.KEYDOWN:
                board.pass_event(event)
            
        
        board.update(event)
        
        main_surface.fill((0, 0, 0))
        board.draw()

        if MODE == 'debug':
            for x in range(STEP, WIDTH, STEP):
                pygame.draw.line(main_surface, (255, 0, 0), (x, 0), (x, HEIGHT))
            for y in range(STEP, HEIGHT, STEP):
                pygame.draw.line(main_surface, (255, 0, 0), (0, y), (WIDTH, y))
        
        pygame.display.update()
        clock.tick(FRAMERATE)


if __name__ == '__main__':
    main()