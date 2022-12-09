import pygame

from Snake import Snake


class Board:
    def __init__(self, surface: pygame.Surface, step: int) -> None:
        self.surface = surface
        self.step = step
        
        self.snakes: list[Snake] = []
        self.speed = 1
    

    def add_snake(self, key_mapping: dict):
        id = len(self.snakes) + 1
        self.snakes.append(Snake(self, id, key_mapping))
    

    def pass_event(self, event):
        for snake in self.snakes:
            snake.pass_event(event)


    def update(self, event):
        '''Oppdaterer alle entiteter på brettet'''
        for snake in self.snakes:
            snake.move()


    def draw(self):
        '''Tegner alle entiteter på brettet'''
        for snake in self.snakes:
            snake.draw()