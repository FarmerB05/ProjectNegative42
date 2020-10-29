import pygame
import time
from settings.settings import Settings
from gui.text import Text

def window(settings):
    if settings.fullscreen:
        screen = pygame.display.set_mode(settings.screen_size, pygame.FULLSCREEN | pygame.HWSURFACE)
    else:
        screen = pygame.display.set_mode(settings.resolution, pygame.RESIZABLE | pygame.DOUBLEBUF)

    return screen

class Game:

    def __init__(self):

        # Settings
        self.settings = Settings()
        self.settings.load()

        self.screen = window(self.settings)
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = self.settings.fps
        self.dt = self.clock.tick(self.fps) / 1000

        self.last_screen = [0, 0]
        self.fps_label = Text(self.screen, int(self.clock.get_fps()), [0, 0, 50, 50], font_size=35)

    def video_event(self, event):
        if event.type == pygame.VIDEORESIZE:
            if not self.settings.fullscreen:
                self.last_screen = [self.screen.get_width(), self.screen.get_height()]
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            return True
        return False

    def update(self):
        self.fps_label = Text(self.screen, int(self.clock.get_fps()), [0, 0, 50, 50], font_size=35)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.fps_label.draw()
