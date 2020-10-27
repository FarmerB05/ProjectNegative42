import pygame
from entity.entity import Entity
from player.player_input import PlayerInput

class Player(Entity, PlayerInput):

    def __init__(self, screen, rect, boundry, speed, health=100, name=None, save_entity=False):
        # Speed Metric: Time it takes to move across entire screen.
        Entity.__init__(self, screen, rect, health=health, name=name, save_entity=save_entity)
        PlayerInput.__init__(self, boundry, speed)

    def scale(self, last, boundry):
        self.speed = int(self.screen.get_width() / 10)
        self.rect = [boundry[0], boundry[1], int(self.screen.get_width() / 30), int(self.screen.get_width() / 30)]
        self.boundry = boundry

    def update(self, dt):
        Entity.update(self)
        x, y = PlayerInput.update_position(self, self.rect, self.settings, dt)
        self.rect[0] = x
        self.rect[1] = y

    def draw(self):
        Entity.draw(self)
