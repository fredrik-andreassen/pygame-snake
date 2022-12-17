import pygame, math


class Food:
    def __init__(self, board, init_frame_nr: int, pos_x: int, pos_y: int, radius: int, color: tuple[int, int, int] = (0, 255, 0)) -> None:
        self.init_frame_nr = init_frame_nr
        self.board = board
        self.pos_x, self.pos_y = pos_x, pos_y
        self.radius = radius
        self.color = color

        self.points = 1
    

    def get_pos(self) -> tuple[int, int]:
        return (self.pos_x, self.pos_y)
    

    def draw(self, frame_nr: int=1) -> None:
        age = frame_nr - self.init_frame_nr
        r = int(self.radius + math.sin(age / 30) * 1.5)
        #pygame.draw.circle(self.board.surface, self.pos_x, self.pos_y, r-1, self.color)
        pygame.draw.circle(self.board.surface, self.color, self.get_pos(), r)