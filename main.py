import pygame
import sys, time

import utils
from Board import Board

STEP = 20

'''
Arguments:
    --debug [FPS]
    --players [count: 1-4]
'''
args = utils.get_args()

try:
    WIDTH = int(args['width'])
    assert not WIDTH % STEP
    print(f'[INIT] Surface width set to {WIDTH}')
except:
    WIDTH = 1600
    print(f'[INIT] Surface width invalid or not given. Using default surface width {WIDTH}')

try:
    HEIGHT = int(args['height'])
    assert not HEIGHT % STEP
    print(f'[INIT] Surface height set to {HEIGHT}')
except:
    HEIGHT = 900
    print(f'[INIT] Surface width invalid or not given. Using default surface height {HEIGHT}')

try:
    FRAMERATE = int(args['debug'])
    MODE = 'debug'
    print(f'[INIT] Debug mode with framerate set to {FRAMERATE}')
except:
    FRAMERATE = 150
    MODE = 'normal'
    print(f'[INIT] Debug request not detected. Using default framerate {FRAMERATE}')

try:
    PLAYER_COUNT = int(args['players'])
    print(f'[INIT] Player count set to {PLAYER_COUNT}')
except:
    PLAYER_COUNT = 1
    print(f'[INIT] Player count invalid or not given. Using default count {PLAYER_COUNT}')


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
    frame_render_times = []

    while True:
        frame_nr += 1
        frame_start_time = time.time()

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
                pygame.draw.line(main_surface, (100, 100, 100), (x, 0), (x, HEIGHT))
            for y in range(STEP, HEIGHT, STEP):
                pygame.draw.line(main_surface, (100, 100, 100), (0, y), (WIDTH, y))

        for snake in board.snakes:
            show_message(main_surface, f'Score: {snake.score}', snake.color_pattern[int(snake.color_pattern_len / 2)], snake.score_pos)
        
        pygame.display.update()

        frame_render_times.append(time.time() - frame_start_time)
        if not frame_nr % int(FRAMERATE / 2):
            mean_frame_render_time = sum(frame_render_times) / len(frame_render_times)
            frame_render_times = []
            print(f'[{frame_nr}] Mean frame render time {round(mean_frame_render_time * 1000, 2)} ms')

        clock.tick(FRAMERATE)


if __name__ == '__main__':
    main()