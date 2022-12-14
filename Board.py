import pygame, random

from Snake import Snake, CollisionException
from Food import Food


class Board:
    def __init__(self, surface: pygame.Surface, step: int) -> None:
        self.surface = surface
        self.step = step
        
        self.snakes: list[Snake] = []
        self.speed = 1

        self.available_food: list[Food] = []
    

    def place_food(self, frame_nr, pos_x=-1, pos_y=-1):
        if pos_x < 0 or pos_y < 0:
            pos_x = random.randrange(self.step, self.surface.get_width(), self.step)
            pos_y = random.randrange(self.step, self.surface.get_height(), self.step)

            attempts = 1
            while (pos_x, pos_y) in [food.get_pos() for food in self.available_food] or (pos_x, pos_y) in [snake.get_pos() for snake in self.snakes]:
                pos_x = random.randrange(self.step, self.surface.get_width(), self.step)
                pos_y = random.randrange(self.step, self.surface.get_height(), self.step)
                attempts += 1

        self.available_food.append(Food(self, frame_nr, pos_x, pos_y, (self.step / 2) - 1))
        print(f'[{self.frame_nr}] Placed food at ({pos_x}, {pos_y}) in {attempts} attempts')


    def assess_food(self, frame_nr) -> None:
        if len(self.available_food) < len(self.snakes) + 1:
            if random.random() < 0.002:
                self.place_food(frame_nr)
    

    def add_snake(self, key_mapping: dict, color: str, init_pos: tuple[int, int], score_pos: tuple[int, int]):
        id = len(self.snakes) + 1
        self.snakes.append(Snake(self, id, key_mapping, color, init_pos, score_pos))
    

    def pass_event(self, event):
        for snake in self.snakes:
            snake.pass_event(event)


    def update(self, frame_nr=0):
        '''Oppdaterer alle entiteter på brettet'''
        self.frame_nr = frame_nr

        for snake in self.snakes:
            snake.move()

            for other_snake in self.snakes:
                if snake.collides(other_snake):
                    if snake.state != 'dead':
                        print(f'[{self.frame_nr}] Snake {snake.id} collided in {other_snake.id}')
                    snake.kill()
            
            for food in self.available_food:
                if snake.get_pos() == food.get_pos():
                    snake.score += food.points
                    self.available_food.remove(food)
                    snake.grow()
                    print(f'[{self.frame_nr}] Snake {snake.id} consumed food at {food.get_pos()}')
        
        self.assess_food(frame_nr)


    def draw(self, frame_nr=1):
        '''Tegner alle entiteter på brettet'''
        for food in self.available_food:
            food.draw(frame_nr)
        
        for snake in self.snakes:
            snake.draw()