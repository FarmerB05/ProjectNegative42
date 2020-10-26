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

        # Health
        self.max_health = health
        self.health = self.max_health
        self.health_rect = [int(self.rect[0] + self.rect[2]/2 - int(self.rect[2] * 1.3) / 2), int(self.rect[1] - int(self.rect[3] / 8) * 3), int(self.rect[2] * 1.3), int(self.rect[3] / 8)]
        self.health_color = (255, 0, 0)

    def health_bar(self):
        self.health_rect = [int(self.rect[0] + self.rect[2]/2 - int(self.rect[2] * 1.3) / 2), int(self.rect[1] - int(self.rect[3] / 8) * 3), int(self.rect[2] * 1.3), int(self.rect[3] / 8)]
        pygame.draw.rect(self.screen, (0, 0, 0), self.health_rect, 1)

        if self.health <= self.max_health * 0.25:
            self.health_color = (255, 0, 0)
        elif self.health <= self.max_health * 0.60:
            self.health_color = (255, 255, 0)
        else:
            self.health_color = (51, 255, 51)

        pygame.draw.rect(self.screen, self.health_color, (self.health_rect[0], self.health_rect[1], (self.health / (self.max_health / self.health_rect[2])), self.health_rect[3]))

    def update(self):
        pass
        
    def draw(self):
        self.health_bar()
        pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
