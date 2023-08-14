import pygame as pg
import pyscreenshot as pss

from main.btn import Buttons
from assets.data import Settings, Colors


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.mouse, self.keys, self.mouse_rel = None, None, None
        self.timer, self.delta_time = 0, 0
        self.surface = pg.Surface(Settings.App.FULLSCREEN_SIZE)
        self.is_fullscreen = Settings.App.BASIC_FULLSCREEN_MODE
        self.width, self.height = None, None
        self.window = None
        self.update_screen_mode()
        self.fs_ratio = 1
        self.is_running = False
        pg.display.set_caption(f'Music: {round(self.clock.get_fps())}')
        self.icon = pg.image.load('assets/img/icon.png')
        pg.display.set_icon(self.icon)
        self.btns = Buttons.load_buttons(self)
        self.current_page = 0

    def update_screen_mode(self):
        self.window = pg.display.set_mode(Settings.App.FULLSCREEN_SIZE,
                                          pg.FULLSCREEN) if self.is_fullscreen \
            else pg.display.set_mode(Settings.App.NOT_FULLSCREEN_SIZE,
                                     pg.RESIZABLE)
        self.width, self.height = self.window.get_size()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
                pg.quit()
                exit()
            elif event.type == pg.KEYUP and self.keys[pg.K_F11]:
                self.is_fullscreen = not self.is_fullscreen
                self.update_screen_mode()
            elif event.type == pg.KEYUP and self.keys[pg.K_F2]:
                img = pss.grab()
                img.save("assets/ss/latestSS.png")
            elif event.type == pg.KEYUP and self.keys[pg.K_ESCAPE]:
                for btn in self.btns:
                    btn.is_pressed = False
                self.current_page = 0

    def update_values(self):
        self.width, self.height = self.window.get_size()
        self.mouse = pg.mouse.get_pos()
        self.mouse_rel = pg.mouse.get_rel()
        self.keys = pg.key.get_pressed()
        self.timer = pg.time.get_ticks()
        self.delta_time = self.clock.tick(Settings.App.FPS)
        self.fs_ratio = self.width // Settings.App.FULLSCREEN_SIZE[0]
        for i in range(len(self.btns)):
            if self.btns[i].is_pressed:
                self.current_page = i + 1

    def draw_page(self):
        if self.current_page == 0:
            for btn in self.btns:
                btn.update()
        else:
            self.btns[self.current_page - 1].draw_page()

    def draw(self):
        self.surface.fill(Colors.grey)
        self.draw_page()
        self.window.blit(pg.transform.scale(self.surface, (self.width, self.height)), (0, 0))
        pg.display.flip()

    def run(self):
        self.is_running = True
        while self.is_running:
            self.draw()
            self.check_events()
            self.update_values()
