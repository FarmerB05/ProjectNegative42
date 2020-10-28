import pygame
import time
from settings.settings import Settings
import json

class Entity:

    def __init__(self, screen, rect, health=100, name=None, save_entity=False):

        # Load settings
        self.settings = Settings()
        self.settings.load()

        self.screen = screen
        self.rect = rect

        # Save
        self.name = name
        self.save_entity = save_entity
        self.file_path = 'data/data.json'

        # Just incase
        if name is None and self.save_entity:
            print('Saved was set to true, but no name was passed.')
            self.save_entity = False

        # Health
        self.max_health = health
        self.health = self.max_health
        self.health_rect = [int(self.rect[0] + self.rect[2]/2 - int(self.rect[2] * 1.3) / 2), int(self.rect[1] - int(self.rect[3] / 8) * 3), int(self.rect[2] * 1.3), int(self.rect[3] / 8)]
        self.health_color = (255, 0, 0)

        # Loadout
        # These if not none will need to be passed into the control script for entity 
        self.weapon = None
        self.helmet = None
        self.chestplate = None
        self.boots = None

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

    """
    # Maybe: Encrypt data so user can't easily edit their items
    def save(self):
        # If the entity doesn't need to be saved, then don't save it.
        # Only things that need to be saved are the Player, and the player's AI's
        # Everything else can be handled in the init
        if self.save_entity:
            with open(self.file_path, 'r') as f:
                data = json.load(f)

            # Save varaibles
            data[self.name] = {}
            # Inventory
            data[self.name]['inventory'] = {}
            data[self.name]['inventory']['value'] = self.inventory
            # Level, etc.

            with open(self.file_path, 'w') as f:
                json.dump(data, f)

    def load(self):
        if self.save_entity:
            with open(self.file_path, 'r') as f:
                data = json.load(f)

            # Load variables
            self.inventory = data[self.name]['inventory']['value']

            print('loaded')
            print(self.inventory)

    """
