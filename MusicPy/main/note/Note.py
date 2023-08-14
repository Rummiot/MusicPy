import pygame as pg

from assets.data import Colors, Data, Labels
from main.note.NoteSize import NoteSize


class Note:
    def __init__(self, id, size: NoteSize, active=False, isMain=False):
        self.id = id
        self.typeId = Data.typeId[id]
        self.name = Data.name[id]
        self.isWhite = True if self.id in (0, 2, 4, 5, 7, 9, 11) else False
        self.isActive = active
        self.isMain = isMain
        self.whiteWidth = size.whiteWidth
        self.whiteHeight = size.whiteHeight
        self.blackWidth = size.blackWidth
        self.blackHeight = size.blackHeight

    def draw(self, surface: pg.Surface, pos):
        if self.isWhite:
            x = pos[0] + self.whiteWidth * self.typeId
            color = Colors.green if self.isMain else Colors.red if self.isActive else Colors.white
            pg.draw.rect(surface, color, (x, pos[1], self.whiteWidth, self.whiteHeight))
            pg.draw.rect(surface, Colors.black, (x, pos[1], self.whiteWidth, self.whiteHeight), 2)
            if self.isMain:
                surface.blit(Labels.white_note.render(self.name, True, Colors.dark_green),
                             (x + self.whiteWidth // 4, pos[1] + self.whiteHeight - self.whiteWidth // 4 * 3))
        else:

            x = pos[0] + self.whiteWidth * (self.typeId + 1) - self.blackWidth // 2 if self.typeId < 2\
                else pos[0] + self.whiteWidth * (self.typeId + 2) - self.blackWidth // 2
            color = Colors.dark_green if self.isMain else Colors.dark_red if self.isActive else Colors.black
            pg.draw.rect(surface, color, (x, pos[1], self.blackWidth, self.blackHeight))
            pg.draw.rect(surface, Colors.black, (x, pos[1], self.blackWidth, self.blackHeight), 2)
            if self.isMain:
                surface.blit(pg.transform.rotate(Labels.black_note.render(self.name, True, Colors.green), -90),
                             (x + self.blackWidth // 10, pos[1] + self.blackHeight // 4))
