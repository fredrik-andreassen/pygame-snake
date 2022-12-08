import pygame

class Board:
    def __init__(self, surface: pygame.Surface, step: int) -> None:
        self.surface = surface
        self.step = step