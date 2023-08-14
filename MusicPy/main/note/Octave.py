from main.note.Note import Note
from main.note.NoteSize import NoteSize


class Octave:
    def __init__(self, pos, noteSize: NoteSize, activeNotes=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), mainNote=-1):
        self.pos = pos
        self.notes = []
        for i in range(12):
            self.notes.append(Note(i, noteSize, activeNotes[i], i == mainNote))
        self.mainNote = mainNote
        self.whiteNotes = [el for el in self.notes if el.isWhite]
        self.blackNotes = [el for el in self.notes if not el.isWhite]

    def draw(self, surface):
        for note in self.whiteNotes:
            note.draw(surface, self.pos)
        for note in self.blackNotes:
            note.draw(surface, self.pos)
