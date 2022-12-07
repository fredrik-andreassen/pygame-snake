import pygame, random, math

from Snake import Snake


class Food:
    def __init__(self, surface: pygame.Surface, target_snake: Snake, color: tuple[int, int, int] = (0, 255, 0)) -> None:
        self.surface = surface
        self.target_snake = target_snake
        self.radius = target_snake.radius - 2
        self.color = color

        available_positions = []
        for x in range(0, surface.get_width(), target_snake.step):
            for y in range(0, surface.get_height(), target_snake.step):
                if not (x, y) in target_snake.get_current_placement():
                    available_positions.append((x, y))

        self.pos_x, self.pos_y = random.choice(available_positions)

        self.points = 1
    

    def get_pos(self) -> tuple[int, int]:
        return (self.pos_x, self.pos_y)
    

    def draw(self, frame_nr: int=1) -> None:
        r = self.radius + (math.sin(frame_nr / 30) * 1.5)
        pygame.draw.circle(self.surface, self.color, self.get_pos(), r)