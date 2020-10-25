import pygame
import time
from settings.settings import Settings

class Entity:

    def __init__(self, screen, rect, health=100):

        # Load settings
        self.settings = Settings()
        self.settings.load()

        self.screen = screen
        self.rect = rect
        self.health = health

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
