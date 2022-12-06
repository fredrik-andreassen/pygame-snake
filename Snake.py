import pygame


class CollisionException(Exception):
    pass


class Snake:
    def __init__(self, surface: pygame.Surface, radius: int = 8, speed: int = 1, color: tuple[int, int, int] = (255, 255, 255)) -> None:
        self.surface = surface
        self.radius = radius
        self.speed = speed
        self.color = color

        self.step = (self.radius * 2) + 2

        self.reset_pos()


    def reset_pos(self) -> None:
        self.pos_x = int(self.surface.get_width() / self.step / 2) * self.step
        self.pos_y = int(self.surface.get_height() / self.step / 2) * self.step

        self.requested_direction = 'none'
        self.current_direction = 'none'

        self.pos_log = [(self.pos_x, self.pos_y)]
        self.len = self.step
    

    def get_pos(self) -> tuple[int, int]:
        return (self.pos_x, self.pos_y)
    

    def request_direction(self, direction: str) -> None:
        if direction not in ['up', 'down', 'right', 'left', 'none']:
            raise ValueError(f'unexpected direction {direction}')

        if direction == self.current_direction:
            return
        elif self.current_direction == 'up' and direction == 'down':
            return
        elif self.current_direction == 'down' and direction == 'up':
            return
        elif self.current_direction == 'right' and direction == 'left':
            return
        elif self.current_direction == 'left' and direction == 'right':
            return
        
        self.requested_direction = direction
    

    def can_change_direction(self) -> bool:
        return not self.pos_x % self.step and not self.pos_y % self.step

    
    def move(self) -> None:
        if self.can_change_direction():
            self.current_direction = self.requested_direction
        
        if self.current_direction == 'up':
            self.pos_y -= self.speed
        elif self.current_direction == 'down':
            self.pos_y += self.speed
        elif self.current_direction == 'right':
            self.pos_x += self.speed
        elif self.current_direction == 'left':
            self.pos_x -= self.speed
        elif self.current_direction == 'none':
            return
        
        if (self.pos_x, self.pos_y) in self.pos_log[-self.len:]:
            raise CollisionException()

        self.pos_log.append((self.pos_x, self.pos_y))
    

    def grow(self) -> None:
        self.len += self.step
        

    def draw(self) -> None:
        for x, y in self.pos_log[-self.len:]:
            pygame.draw.circle(self.surface, self.color, (x, y), self.radius)