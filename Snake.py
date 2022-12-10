import pygame


class CollisionException(Exception):
    pass


class Snake:
    def __init__(self, board, id: int, key_mapping: dict, color: str, init_pos: tuple[int, int], score_pos: tuple[int, int]) -> None:
        self.board = board
        self.id = id
        self.key_mapping = key_mapping
        self.init_pos_x, self.init_pos_y = init_pos
        self.score_pos = score_pos

        self.radius = board.step / 2

        self.generate_color_pattern(color)

        self.reset()
    

    def generate_color_pattern(self, color: str = '') -> None:
        darkest, brightest = 80, 170
        color_pattern = [(i, i, i) for i in range(darkest, brightest)]
        
        if color:
            if color == 'grey' or color == 'gray':
                color_pattern = [(120, 120, 120)]
            if color == 'red':
                color_pattern = [(255, i, i) for i in range(darkest, brightest)]
            if color == 'green':
                color_pattern = [(i, 255, i) for i in range(darkest, brightest)]
            if color == 'blue':
                color_pattern = [(i, i, 255) for i in range(darkest, brightest)]
            if color == 'yellow':
                color_pattern = [(255, 255, i) for i in range(darkest, brightest)]
            if color == 'purple':
                color_pattern = [(255, i, 255) for i in range(darkest, brightest)]

        self.color_pattern = color_pattern + list(reversed(color_pattern))
        self.color_pattern_len = len(self.color_pattern)


    def kill(self) -> None:
        self.state = 'dead'
        self.generate_color_pattern('gray')

    def reset(self) -> None:
        self.pos_x = self.init_pos_x
        self.pos_y = self.init_pos_y

        self.requested_direction = 'none'
        self.current_direction = 'none'

        self.pos_log = [(self.pos_x, self.pos_y)]
        self.allowed_len = self.board.step
        self.current_len = 1

        self.state = 'alive'
        self.score = 0
    

    def get_pos(self) -> tuple[int, int]:
        return (self.pos_x, self.pos_y)
    

    def get_current_visual_placement(self) -> list[tuple[int, int]]:
        return self.pos_log[-int(self.current_len):]
    

    def get_current_placement(self) -> list[tuple[int, int]]:
        return self.pos_log[-int(self.current_len)-1:]
    

    def collides(self, other_snake):
        return self.get_pos() in other_snake.get_current_placement()[:-1]
    

    def pass_event(self, event) -> None:
        if event.type == pygame.KEYDOWN and event.key in self.key_mapping:
            self.request_direction(self.key_mapping[event.key])

    
    def request_direction(self, direction: str) -> None:
        if direction not in ['up', 'down', 'right', 'left', 'none']:
            raise ValueError(f'snake {self.id} got unexpected direction {direction}')
        
        print(f'[{self.board.frame_nr}] Snake {self.id} received request {direction}')

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
        return not self.pos_x % self.board.step and not self.pos_y % self.board.step
    

    def move(self) -> None:
        if self.state == 'dead':
            return

        if self.can_change_direction() and self.current_direction != self.requested_direction:
            self.current_direction = self.requested_direction
            print(f'[{self.board.frame_nr}] Snake {self.id} changed direction {self.current_direction}')
        
        if self.current_direction == 'up':
            self.pos_y -= self.board.speed
        elif self.current_direction == 'down':
            self.pos_y += self.board.speed
        elif self.current_direction == 'right':
            self.pos_x += self.board.speed
        elif self.current_direction == 'left':
            self.pos_x -= self.board.speed
        elif self.current_direction == 'none':
            return
        
        if self.pos_y < 0:
            self.pos_y = self.board.surface.get_height()
        elif self.pos_y > self.board.surface.get_height():
            self.pos_y = 0
        elif self.pos_x < 0:
            self.pos_x = self.board.surface.get_width()
        elif self.pos_x > self.board.surface.get_width():
            self.pos_x = 0
        
        if self.current_len < self.allowed_len:
            if self.allowed_len == self.board.step:
                self.current_len += self.board.speed
            else:
                self.current_len += 0.05 * self.board.speed

        self.pos_log.append((self.pos_x, self.pos_y))


    def grow(self) -> None:
        self.allowed_len += self.board.step
        

    def draw(self) -> None:
        for i, (x, y) in enumerate(self.get_current_visual_placement()):
            color = self.color_pattern[i % self.color_pattern_len]
            pygame.draw.circle(self.board.surface, color, (x, y), self.radius)