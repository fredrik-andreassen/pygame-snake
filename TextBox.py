import pygame

class TextBox:
    def __init__(self, surface: pygame.Surface,
                 text: str,
                 size: int,
                 x_pos: int,
                 y_pos: int,
                 width: int,
                 height: int,
                 bg_color: tuple[int, int, int],
                 fg_color: tuple[int, int, int]
                 ) -> None:
        
        self.surface = surface
        self.text = text
        self.size = size
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fg_color = fg_color

        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.font_style = pygame.font.SysFont(None, self.size)
    

    def get_pos(self) -> tuple[int, int]:
        return (self.x_pos, self.y_pos)
    

    def draw(self):
        pygame.draw.rect(self.surface, self.bg_color, self.rect)
        self.surface.blit(self.font_style.render(self.text, True, self.fg_color), self.get_pos())