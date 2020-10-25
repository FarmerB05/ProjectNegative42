import pygame
from entity.entity import Entity
from player.player_input import PlayerInput

class Player(Entity, PlayerInput):

    def __init__(self, screen, rect, boundry, speed, health=100):
        # Speed Metric: Time it takes to move across entire screen.
        Entity.__init__(self, screen, rect, health=health)
        PlayerInput.__init__(self, boundry, speed)

    def scale(self):
        self.boundry = [0, 0, self.screen.get_width(), self.screen.get_height()]
        self.speed = int(self.screen.get_width() / 5)
        self.rect[2] = int(self.screen.get_width() / 30)
        self.rect[3] = int(self.screen.get_width() / 30)

    def update(self, dt):
        Entity.update(self)
        x, y = PlayerInput.update_position(self, self.rect, self.settings, dt)
        self.rect[0] = x
        self.rect[1] = y

    def draw(self):
        Entity.draw(self)
