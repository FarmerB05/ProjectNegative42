import pygame
from inventory.inventory import Inventory
from convert.convert import str_2_item
from convert.convert import scale_h
import random

class InventoryDisplay:

    def __init__(self, screen):
        self.screen = screen
        self.inventory = Inventory()

    def update(self):
        pass

    # Draw functions

    def global_inventory(self):
        # Draw box
        # Scaling is going to be a fucking pain
        # Drawing in center of screen for time being

        inventory_rect = [int(self.screen.get_width()/2 - int(self.screen.get_width()/2)/2), int(self.screen.get_height()/2 - scale_h([1, 1], int(self.screen.get_width()/2))/2), int(self.screen.get_width()/2), scale_h([1, 1], int(self.screen.get_width()/2))]

        # Create grid
        grid = []
        length = 10
        margin = 10
        w = int((inventory_rect[2] - (margin * length + 1)) / length)
        h = int((inventory_rect[3] - (margin * length + 1)) / length)
        counter_2 = 0
        counter_1 = 0
        for i in range(len(self.inventory.inventory)):
            if i % length == 0 and i > 0:
                counter_2 += 1
                counter_1 = 0

            grid.append([inventory_rect[0] + (margin) + (margin * counter_1) + (w * counter_1), inventory_rect[1] + (margin) + (margin * counter_2) + (h * counter_2), w, w])

            counter_1 += 1

        pygame.draw.rect(self.screen, (255, 255, 255), inventory_rect)

        for i in range(len(self.inventory.inventory)):
            pygame.draw.rect(self.screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), grid[i], 0)
            self.screen.blit(pygame.transform.scale(str_2_item(self.inventory.inventory[i], 1).sprite, (w, w)), (grid[i][0], grid[i][1]))


    def draw(self):
        self.global_inventory()
