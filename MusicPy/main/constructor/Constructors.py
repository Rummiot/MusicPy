from assets.data import Data
from main.constructor.Constructor import Constructor
from main.note.NoteSize import NoteSize

padding = 75
note_size = NoteSize(60, 180, 40, 120)

MAJOR_GAMMA = Constructor(padding, note_size, Data.majorGamma)
MINOR_GAMMA = Constructor(padding, note_size, Data.minorGamma)
MAJOR_3 = Constructor(padding, note_size, Data.major3)
MINOR_3 = Constructor(padding, note_size, Data.minor3)
DIMINISHED = Constructor(padding, note_size, Data.diminished)
AUGMENTED = Constructor(padding, note_size, Data.augmented)
MAJOR_7 = Constructor(padding, note_size, Data.major7)
MINOR_7 = Constructor(padding, note_size, Data.minor7)
DOMINANT_7 = Constructor(padding, note_size, Data.dominant7)
AUGMENTED_7 = Constructor(padding, note_size, Data.augmented)
DOMINANT_7_B_5 = Constructor(padding, note_size, Data.dominant7b5)
MAJ_7 = Constructor(padding, note_size, Data.maj7)

Cnstrs = [MAJOR_GAMMA, MINOR_GAMMA, MAJOR_3, MINOR_3,
          DIMINISHED, AUGMENTED, MAJOR_7, MINOR_7,
          DOMINANT_7, AUGMENTED_7, DOMINANT_7_B_5, MAJ_7]
