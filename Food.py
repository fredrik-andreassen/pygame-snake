import pygame, random

from Snake import Snake


class Food:
    def __init__(self, surface: pygame.Surface, target_snake: Snake, radius: int = 7, color: tuple[int, int, int] = (0, 255, 0)) -> None:
        self.surface = surface
        self.target_snake = target_snake
        self.radius = radius
        self.color = color

        self.pos_x = random.randrange(target_snake.step, surface.get_width(), target_snake.step)
        self.pos_y = random.randrange(target_snake.step, surface.get_height(), target_snake.step)
    

    def get_pos(self) -> tuple[int, int]:
        return (self.pos_x, self.pos_y)
    

    def draw(self) -> None:
        pygame.draw.circle(self.surface, self.color, self.get_pos(), self.radius)