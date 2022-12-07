import pygame, sys, time

from Snake import Snake, CollisionException
from Food import Food

if len(sys.argv) == 3:
    display_width = int(sys.argv[1])
    display_height = int(sys.argv[2])
else:
    display_height = 720
    display_width = 1280

framerate = 200

red = (255, 0, 0)
green = (0, 255, 00)
blue = (0, 0, 255)

black = (0, 0, 0)
white = (255, 255, 255)

yellow = (255, 255, 0)
orange = (255, 130, 0)


def show_message(display: pygame.Surface, message: str, color: tuple[int, int, int], position: tuple[int, int], size: int = 50):
    font_style = pygame.font.SysFont(None, size)
    display.blit(font_style.render(message, True, color), position)


def main():
    
    pygame.init()

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('pygame-snake')
    clock = pygame.time.Clock()

    snake = Snake(display, speed=1, radius=10)
    available_food = [Food(display, snake)]

    score = 0
    frame_nr = 0

    while True:
        frame_nr += 1

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print('QUIT event triggered')
                pygame.quit()
                sys.exit(0)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.request_direction('left')
                elif event.key == pygame.K_RIGHT:
                    snake.request_direction('right')
                elif event.key == pygame.K_UP:
                    snake.request_direction('up')
                elif event.key == pygame.K_DOWN:
                    snake.request_direction('down')

        display.fill(black)

        for food in available_food:
            food.draw(frame_nr=frame_nr)

        try:
            snake.move()
            snake.draw()
        except CollisionException:
            print(f'GAME OVER! Score: {score}')
            snake.draw()
            show_message(display, 'GAME OVER', red, (display_width/2, display_height/2))
            pygame.display.update()
            time.sleep(3)

            snake.reset()
            available_food = [Food(display, snake)]
            score = 0

        for food in available_food:
            if snake.get_pos() == food.get_pos():
                score += food.points
                snake.grow()
                print(f'Consumed food at {food.get_pos()}')
                available_food.remove(food)

                new_food = Food(display, snake)
                available_food.append(new_food)
                print(f'Food placed at {new_food.get_pos()}')
        
        show_message(display, f'Score: {score}', (150, 150, 150), (5, 5), size=30)

        pygame.display.update()

        clock.tick(framerate)


if __name__ == '__main__':
    main()