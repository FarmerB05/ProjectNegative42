import pygame
from item.item import Item

class Sword(Item):

    def __init__(self, sprite):
        super().__init__(sprite) #Just pass in a pygame image for now
