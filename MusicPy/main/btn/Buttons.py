from main.constructor import Constructors
from main.btn.Button import Button

SIZE = 250, 100
PADDING = 50


def load_buttons(app):
    buttons = [Button(app, SIZE, (535 + (i - 1) * PADDING + i * SIZE[0], 265 + (j - 1) * PADDING + j * SIZE[1]),
                      Constructors.Cnstrs[i * 4 + j], i * 4 + j) for i in range(3) for j in range(4)]
    return buttons
