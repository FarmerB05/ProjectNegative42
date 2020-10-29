import pygame
from inventory.inventory import Inventory
from convert.convert import str_2_item
from convert.convert import scale_h
import random
from gui.text import Text
from gui.button import Button
import time

class InventoryDisplay:

    def __init__(self, screen):
        self.screen = screen
        self.length = 4
        self.margin = 5
        self.inventory = Inventory()

        # Inventory elements
        # Inventory background
        # 1. Global inventory
        self.inventory_rect = [self.screen.get_width()/2 - int(self.screen.get_width()/4/2), 10, int(self.screen.get_width()/4), scale_h([1, 1], int(self.screen.get_width()/4))]
        self.page = 0

        # Text and Buttons
        self.button_page_up = Button('>', [self.inventory_rect[0] + self.inventory_rect[2], self.inventory_rect[1], int(self.inventory_rect[2]/6), self.inventory_rect[3]], self.screen, colors=[(105,105,105), (169,169,169)])
        self.button_page_down = Button('<', [self.inventory_rect[0] - int(self.inventory_rect[2]/6), self.inventory_rect[1], int(self.inventory_rect[2]/6), self.inventory_rect[3]], self.screen, colors=[(105,105,105), (169,169,169)])
        self.page_text = Text(self.screen, str(self.page + 1), [self.inventory_rect[0], self.inventory_rect[1] - 50, self.inventory_rect[2], 50])
        self.button_delay_1 = time.time() + 0.15
        self.button_delay_2 = time.time() + 0.15

        # 2. Preview
        self.preview_image = None
        self.preview_rect = []

        self.box_width = None
        # slots
        # weapon
        self.weapon_rect = []
        self.weapon_placeholder = None

        # helmet
        self.helmet_rect = []
        self.helmet_placeholder = None

        # chestplate
        self.chestplate_rect = []
        self.chestplate_placeholder = None

        # boots
        self.boots_rect = []
        self.boots_placeholder = None

        # Grid
        self.grid = []

         # Set value to everything
        self.scale()

    def scale(self):
        self.inventory_rect = [self.screen.get_width()/2 - int(self.screen.get_width()/3.5/2), 10, int(self.screen.get_width()/3.5), scale_h([1, 1], int(self.screen.get_width()/3.5))]
        self.button_page_up.rect = [self.inventory_rect[0] + self.inventory_rect[2], self.inventory_rect[1], int(self.inventory_rect[2]/6), self.inventory_rect[3]]
        self.button_page_down.rect = [self.inventory_rect[0] - int(self.inventory_rect[2]/6), self.inventory_rect[1], int(self.inventory_rect[2]/6), self.inventory_rect[3]]
        self.page_text.rect = [self.inventory_rect[0], self.inventory_rect[1] - 50, self.inventory_rect[2], 50]

        # preview
        self.preview_rect = [self.screen.get_width()/2 - int(self.screen.get_width()/10/2), self.inventory_rect[1] + self.inventory_rect[3] + 15, int(self.screen.get_width()//10), scale_h([12, 20], int(self.screen.get_width()//10))]

        margin = 5
        self.box_width = int((self.preview_rect[3] - (margin*3))/3)
        # weapon
        self.weapon_rect = [
            self.preview_rect[0] + self.preview_rect[2] + int(self.box_width/5),
            self.preview_rect[1] + self.preview_rect[3]/2 - int(self.box_width/2), # this height /2
            self.box_width,
            self.box_width
        ]

        self.weapon_placeholder = pygame.transform.scale(pygame.image.load('weapon_placeholder.png'), (self.weapon_rect[2], self.weapon_rect[3]))

        # Armour slots
        # helmet
        self.helmet_rect = [

            self.preview_rect[0] - self.box_width - int(self.box_width/5),
            self.preview_rect[1],
            self.box_width,
            self.box_width

        ]

        self.helmet_placeholder = pygame.transform.scale(pygame.image.load('helmet_placeholder.png'), (self.helmet_rect[2], self.helmet_rect[3]))

        # chestplate
        self.chestplate_rect = [

            self.preview_rect[0] - self.box_width - int(self.box_width/5),
            self.preview_rect[1] + self.preview_rect[3]/2 - int(self.box_width/2),
            self.box_width,
            self.box_width

        ]

        self.chestplate_placeholder = pygame.transform.scale(pygame.image.load('chestplate_placeholder.png'), (self.chestplate_rect[2], self.chestplate_rect[3]))

        # boots
        self.boots_rect = [

            self.preview_rect[0] - self.box_width - int(self.box_width/5),
            self.preview_rect[1] + self.preview_rect[3] - self.box_width,
            self.box_width,
            self.box_width

        ]

        self.boots_placeholder = pygame.transform.scale(pygame.image.load('boots_placeholder.png'), (self.boots_rect[2], self.boots_rect[3]))

        # Update Grid
        self.update_grid()

    # update functions
    def update_grid(self):
        self.grid = []
        w = int((self.inventory_rect[2] - (self.margin * self.length + 1)) / self.length)
        h = int((self.inventory_rect[3] - (self.margin * self.length + 1)) / self.length)

        counter_2 = 0
        counter_1 = 0
        for i in range(self.length**2):
            if i % self.length == 0 and i > 0:
                counter_2 += 1
                counter_1 = 0
            self.grid.append([self.inventory_rect[0] + (self.margin) + (self.margin * counter_1) + (w * counter_1), self.inventory_rect[1] + (self.margin) + (self.margin * counter_2) + (h * counter_2), w, w])
            counter_1 += 1

        print('updated_grid')

    def update(self):
        self.button_page_up.update()
        self.button_page_down.update()
        self.page_text.update()
        self.page_text.text = str(self.page + 1)

        if self.button_page_up.click() and time.time() >= self.button_delay_1:
            if self.length**2 * self.page < len(self.inventory.inventory) - self.length**2:
                self.page += 1
                self.update_grid()
                self.button_delay_1 = time.time() + 0.15

                print(self.page)

        if self.button_page_down.click() and time.time() >= self.button_delay_2:
            if self.length**2 * self.page > 0:
                self.page -= 1
                self.update_grid()
                self.button_delay_2 = time.time() + 0.15
                print(self.page)

    # Draw functions

    def global_inventory(self):
        # Draw box
        # Scaling is going to be a fucking pain
        # Drawing in center of screen for time being
        self.update_grid()
        pygame.draw.rect(self.screen, (255, 255, 255), self.inventory_rect)

        self.button_page_up.draw()
        self.button_page_down.draw()
        self.page_text.draw()

        for i in range(self.length**2):
            #random.randint(1, 254), random.randint(1, 254), random.randint(1, 254)
            pygame.draw.rect(self.screen, (self.page * 10, 0, 60), self.grid[i])
            try:
                self.screen.blit(pygame.transform.scale(str_2_item(self.inventory.inventory[i + self.length**2 * self.page], 1).sprite, (self.grid[i][2], self.grid[i][3])), (self.grid[i][0], self.grid[i][1]))
            except:
                self.screen.blit(pygame.transform.scale(str_2_item(self.inventory.inventory[len(self.inventory.inventory) - 1], 1).sprite, (self.grid[i][2], self.grid[i][3])), (self.grid[i][0], self.grid[i][1]))
                break

    def draw(self):
        self.global_inventory()
        pygame.draw.rect(self.screen, (133, 0, 133), self.preview_rect)
        pygame.draw.rect(self.screen, (133, 0, 133), self.weapon_rect)
        self.screen.blit(self.weapon_placeholder, (self.weapon_rect[0], self.weapon_rect[1]))

        pygame.draw.rect(self.screen, (133, 0, 133), self.helmet_rect)
        self.screen.blit(self.helmet_placeholder, (self.helmet_rect[0], self.helmet_rect[1]))

        pygame.draw.rect(self.screen, (133, 0, 133), self.chestplate_rect)
        self.screen.blit(self.chestplate_placeholder, (self.chestplate_rect[0], self.chestplate_rect[1]))

        pygame.draw.rect(self.screen, (133, 0, 133), self.boots_rect)
        self.screen.blit(self.boots_placeholder, (self.boots_rect[0], self.boots_rect[1]))
