import pygame
import sys

from Board import Board


WIDTH = 1600
HEIGHT = 900

MODE = 'normal'
FRAMERATE = 150

if len(sys.argv) >= 2:
    if sys.argv[1] == 'debug':
        MODE = 'debug'
        try:
            FRAMERATE = int(sys.argv[2])
        except:
            FRAMERATE = 10

STEP = 20
PLAYER_COUNT = 3


def show_message(display: pygame.Surface, message: str, color: tuple[int, int, int], position: tuple[int, int], size: int = 40):
    font_style = pygame.font.SysFont(None, size)
    display.blit(font_style.render(message, True, color), position)


def main():
    pygame.init()

    main_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('pygame-snake')
    clock = pygame.time.Clock()

    board = Board(main_surface, STEP)

    key_mappings = [{pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_RIGHT: 'right', pygame.K_LEFT: 'left'},
                    {pygame.K_w: 'up', pygame.K_s: 'down', pygame.K_d: 'right', pygame.K_a: 'left'},
                    {pygame.K_t: 'up', pygame.K_g: 'down', pygame.K_h: 'right', pygame.K_f: 'left'},
                    {pygame.K_i: 'up', pygame.K_k: 'down', pygame.K_l: 'right', pygame.K_j: 'left'}]
    
    colors = ['blue', 'red', 'yellow', 'purple']

    start_positions = [(STEP * 10,           STEP * 10),
                       (WIDTH - (STEP * 10), HEIGHT - (STEP * 10)),
                       (WIDTH - (STEP * 10), STEP * 10),
                       (STEP * 10,           HEIGHT - (STEP * 10))]
    
    score_positions = [(STEP,            STEP),
                       (WIDTH - (STEP * 7), HEIGHT - (STEP * 2)),
                       (WIDTH - (STEP * 7), STEP),
                       (STEP,            HEIGHT - (STEP * 2))]
    
    for i in range(PLAYER_COUNT):
        board.add_snake(key_mappings[i], colors[i], start_positions[i], score_positions[i])

    frame_nr = 0
    while True:
        frame_nr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(f'[{frame_nr}] QUIT event triggered')
                pygame.quit()
                sys.exit(0)
            
            if event.type == pygame.KEYDOWN:
                board.pass_event(event)
            
        
        board.update(frame_nr)
        
        main_surface.fill((0, 0, 0))
        board.draw(frame_nr)

        if MODE == 'debug':
            for x in range(STEP, WIDTH, STEP):
                pygame.draw.line(main_surface, (255, 0, 0), (x, 0), (x, HEIGHT))
            for y in range(STEP, HEIGHT, STEP):
                pygame.draw.line(main_surface, (255, 0, 0), (0, y), (WIDTH, y))

        for snake in board.snakes:
            show_message(main_surface, f'Score: {snake.score}', snake.color_pattern[int(snake.color_pattern_len / 2)], snake.score_pos)
        
        pygame.display.update()
        clock.tick(FRAMERATE)


if __name__ == '__main__':
    main()