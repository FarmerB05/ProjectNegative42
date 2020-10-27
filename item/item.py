import pygame
import time

class Item:

    def __init__(self, sprite, rarity, level, stats):
        self.sprite = sprite
        self.rarity = rarity # (subject to change later) common, uncommon, rare, epic, legendary
        self.level = level # 0, 1, 2, 3, etc.

        self.damage = damage

    def update(self):
        pass

class Ranged:

    def __init__(self):
        pass
