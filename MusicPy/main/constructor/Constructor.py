import pygame as pg

from assets.data import Settings, Colors
from main.note.Octave import Octave
from main.note.NoteSize import NoteSize


class Constructor:
    def __init__(self, padding, note_size: NoteSize, pattern):
        self.pattern = pattern
        self.padding = padding
        self.note_size = note_size
        self.octaves = []
        self.offset = (Settings.App.FULLSCREEN_SIZE[0] - (3 * 7 * self.note_size.whiteWidth + 2 * self.padding)) // 2, \
                      (Settings.App.FULLSCREEN_SIZE[1] - (4 * self.note_size.whiteHeight + 3 * self.padding)) // 2
        for i in range(4):
            for j in range(3):
                self.octaves.append(Octave((self.offset[0] + j * (self.note_size.whiteWidth * 7 + padding),
                                            (self.offset[1] + i * (self.note_size.whiteHeight + padding))),
                                           self.note_size, self.activeNotes(i * 3 + j), i * 3 + j))

    def activeNotes(self, mainNote):
        return self.pattern[-mainNote:] + self.pattern[:-mainNote]

    def draw(self, surface: pg.Surface):
        surface.fill(Colors.grey)
        for octave in self.octaves:
            octave.draw(surface)
