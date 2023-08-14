from ctypes import windll


class App:
    FULLSCREEN_SIZE = windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)
    NOT_FULLSCREEN_SIZE = 1024, 576
    FPS = -1
    BASIC_FULLSCREEN_MODE = True
