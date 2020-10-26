import pygame
import time
from settings.settings import Settings

def window(settings):
    if settings.fullscreen:
        screen = pygame.display.set_mode(settings.screen_size, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(settings.resolution)

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

    def video_event(self, event):
        if event.type == pygame.VIDEORESIZE:
            if not self.settings.fullscreen:
                self.last_screen = [self.screen.get_width(), self.screen.get_height()]
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            return True
        return False

    def update(self):
        pass

    def draw(self):
        pass
