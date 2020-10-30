import pygame
import time

class Item:

    def __init__(self, sprite, type, level, rarity, selected):
        self.sprite = sprite
        self.type = type
        self.level = level
        self.rarity = rarity
        self.selected = selected

    def update(self):
        pass

class Sword(Item):

    def __init__(self, level, rarity, selected=False):
        super().__init__(pygame.image.load('sword.png'), 'weapon', level=level, rarity=rarity, selected=selected)

class Helmet(Item):

    def __init__(self, level, rarity, selected=False):
        super().__init__(pygame.image.load('helmet.png'), 'helmet', level=level, rarity=rarity, selected=selected)

class Chestplate(Item):

    def __init__(self, level, rarity, selected=False):
        super().__init__(pygame.image.load('chestplate.png'), 'chestplate', level=level, rarity=rarity, selected=selected)

class Boots(Item):

    def __init__(self, level, rarity, selected=False):
        super().__init__(pygame.image.load('boots.png'), 'boots', level=level, rarity=rarity, selected=selected)
