import pygame as pg

from assets.data import Colors, Data, Labels
from main.constructor.Constructor import Constructor


class Button:
    def __init__(self, app, size, pos, pattern: Constructor, id):
        self.app = app
        self.width, self.height = size
        self.normal_size = size
        self.pos = list(pos)
        self.normal_pos = pos
        self.pattern = pattern
        self.id = id
        self.rectangle = pg.rect.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.label_rect = Labels.btn.render(str(Data.name[self.id]), True, Colors.black).get_rect(
            center=(self.pos[0] + self.width // 2, self.pos[1] + self.width // 5))
        self.is_hovered, self.is_pressed = False, False

    def draw(self):
        pg.draw.rect(self.app.surface, Colors.white, self.rectangle)
        pg.draw.rect(self.app.surface, Colors.button_border, self.rectangle, width=10) \
            if not self.is_hovered else \
            pg.draw.rect(self.app.surface, Colors.button_border_hover, self.rectangle, width=10)
        self.app.surface.blit(Labels.btn.render(str(Data.name[self.id]), True, Colors.black), self.label_rect)

    def draw_page(self):
        self.pattern.draw(self.app.surface)

    def hover_update(self):
        if self.app.mouse is not None:
            self.is_hovered = self.rectangle.collidepoint(self.app.mouse[0], self.app.mouse[1])

    def press_update(self):
        if self.is_hovered and pg.mouse.get_pressed()[0]:
            self.is_pressed = True

    def update(self):
        self.width, self.height = self.app.fs_ratio * self.normal_size[0], self.app.fs_ratio * self.normal_size[1]
        self.pos = self.app.fs_ratio * self.normal_pos[0], self.app.fs_ratio * self.normal_pos[1]
        self.hover_update()
        self.press_update()
        self.draw()
