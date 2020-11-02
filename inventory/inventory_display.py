import pygame
from inventory.inventory import Inventory
from convert.convert import str_2_item
from convert.convert import scale_h
import random
from gui.text import Text
from gui.button import Button
import time

class InventoryDisplay:

    def __init__(self, screen, entities):
        self.screen = screen
        self.entities = entities # list with objects
        self.current_entity = -1 # what current entity are we working with
        self.length = 4
        self.margin = int(self.screen.get_width()/288)
        self.inventory = Inventory()

        # Inventory elements
        # Inventory background
        # 1. Global inventory
        self.inventory_rect = [self.screen.get_width()/2 - int(self.screen.get_width()/3.5/2), int(self.screen.get_height()/3), int(self.screen.get_width()/3.5), scale_h([1, 1], int(self.screen.get_width()/3.5))]
        self.page = 0

        # Text and Buttons
        self.button_page_up = Button('>', [self.inventory_rect[0] + self.inventory_rect[2], self.inventory_rect[1], int(self.inventory_rect[2]/6), self.inventory_rect[3]], self.screen, colors=[(105,105,105), (169,169,169)])
        self.button_page_down = Button('<', [self.inventory_rect[0] - int(self.inventory_rect[2]/6), self.inventory_rect[1], int(self.inventory_rect[2]/6), self.inventory_rect[3]], self.screen, colors=[(105,105,105), (169,169,169)])
        self.page_text = Text(self.screen, str(self.page + 1), [self.inventory_rect[0], self.inventory_rect[1] - 50, self.inventory_rect[2], 50], font_size=42)
        self.button_delay_1 = time.time() + 0.15
        self.button_delay_2 = time.time() + 0.15
        self.click_delay = time.time() + 0.15

        # 2. Preview
        self.preview_image = None
        self.preview_rect = []

        self.box_width = None
        # slots
        # weapon
        self.weapon_rect = []
        self.weapon_placeholder = None
        self.weapon_equipped = None

        # helmet
        self.helmet_rect = []
        self.helmet_placeholder = None
        self.helmet_equipped = None

        # chestplate
        self.chestplate_rect = []
        self.chestplate_placeholder = None
        self.chestplate_equipped = None

        # boots
        self.boots_rect = []
        self.boots_placeholder = None
        self.boots_equipped = None

        # Center box
        self.center_box = []

        # Grid
        self.grid = []

        self.mouse_down = False

         # Set value to everything
        self.scale()

    def scale(self):
        self.inventory_rect = [self.screen.get_width()/2 - int(self.screen.get_width()/3.5/2), 0, int(self.screen.get_width()/3.5), scale_h([1, 1], int(self.screen.get_width()/3.5))]

        self.center_box = [
            self.screen.get_width()/2 - (self.inventory_rect[2] + (int(self.inventory_rect[2]/6)*2))/2,
            self.screen.get_height()/2 - (self.inventory_rect[3] + scale_h([12, 20], int(self.screen.get_width()//10)) + 15)/2,
            self.inventory_rect[2] + (int(self.inventory_rect[2]/6)*2),
            self.inventory_rect[3] + scale_h([12, 20], int(self.screen.get_width()//10)) + 15

        ]

        self.inventory_rect[1] = self.center_box[1]

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

        if self.inventory_rect == self.center_box[0]:
            pass
        else:
            self.inventory_rect[1] = self.center_box[1]

        # Update Grid
        self.margin = int(self.screen.get_width()/288)
        self.update_grid()

    def item_click(self):
        if pygame.mouse.get_pressed()[0]:
            if self.mouse_down == False:
                mx, my = pygame.mouse.get_pos()
                for i in range(self.length**2):
                    # self.length**2 * self.page
                    if mx >= self.inventory_rect[0] and mx <= self.inventory_rect[0] + self.inventory_rect[2] and my >= self.inventory_rect[1] and my <= self.inventory_rect[1] + self.inventory_rect[3]:
                        if mx >= self.grid[i][0] and mx <= self.grid[i][0] + self.grid[i][2] and my >= self.grid[i][1] and my <= self.grid[i][1] + self.grid[i][3]:
                            try:
                                wow = self.inventory.inventory[i + self.length**2 * self.page]
                                if self.inventory.inventory[i + self.length**2 * self.page][3]:
                                    self.inventory.inventory[i + self.length**2 * self.page][3] = False
                                    if str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'weapon':
                                        self.weapon_equipped = None
                                    elif str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'helmet':
                                        self.helmet_equipped = None
                                    elif str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'chestplate':
                                        self.chestplate_equipped = None
                                    elif str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'boots':
                                        self.boots_equipped = None
                                elif str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'weapon':
                                    if not self.weapon_equipped:
                                        self.inventory.inventory[i + self.length**2 * self.page][3] = True
                                        self.weapon_equipped = self.inventory.inventory[i + self.length**2 * self.page]
                                elif str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'helmet':
                                    if not self.helmet_equipped:
                                        self.inventory.inventory[i + self.length**2 * self.page][3] = True
                                        self.helmet_equipped = self.inventory.inventory[i + self.length**2 * self.page]
                                elif str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'chestplate':
                                    if not self.chestplate_equipped:
                                        self.inventory.inventory[i + self.length**2 * self.page][3] = True
                                        self.chestplate_equipped = self.inventory.inventory[i + self.length**2 * self.page]
                                elif str_2_item(wow[0], wow[1], wow[2], wow[3]).type == 'boots':
                                    if not self.boots_equipped:
                                        self.inventory.inventory[i + self.length**2 * self.page][3] = True
                                        self.boots_equipped = self.inventory.inventory[i + self.length**2 * self.page]
                            except:
                                pass

                            break
                    else:
                        item_slots = [[self.weapon_rect, self.weapon_equipped], [self.helmet_rect, self.helmet_equipped], [self.chestplate_rect, self.chestplate_equipped], [self.boots_rect, self.boots_equipped]]
                        for j in range(len(item_slots)):
                            if item_slots[j][1]:
                                if mx >= item_slots[j][0][0] and mx <= item_slots[j][0][0] + item_slots[j][0][2] and my >= item_slots[j][0][1] and my <= item_slots[j][0][1] + item_slots[j][0][3]:
                                    item_slots[j][1][3] = False
                                    item_slots[j][1] = None
                                    break

                        self.weapon_equipped = item_slots[0][1]
                        self.helmet_equipped = item_slots[1][1]
                        self.chestplate_equipped = item_slots[2][1]
                        self.boots_equipped = item_slots[3][1]

                self.mouse_down = True
        else:
            self.mouse_down = False

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

    def update(self):
        self.item_click()

        # update entity inventory
        self.entities[self.current_entity].weapon = self.weapon_equipped
        self.entities[self.current_entity].helmet = self.helmet_equipped
        self.entities[self.current_entity].chestplate = self.chestplate_equipped
        self.entities[self.current_entity].boots = self.boots_equipped

        # see what entity is selected


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
            try:
                wow = self.inventory.inventory[i + self.length**2 * self.page]
                if wow[3]:
                    pygame.draw.rect(self.screen, (255, 71, 213), self.grid[i])
                else:
                    pygame.draw.rect(self.screen, (30, 0, 60), self.grid[i])

                self.screen.blit(pygame.transform.scale(str_2_item(wow[0], wow[1], wow[2], wow[3]).sprite, (self.grid[i][2], self.grid[i][3])), (self.grid[i][0], self.grid[i][1]))
            except:
                break

    def draw(self):

        #pygame.draw.rect(self.screen, (133, 54, 133), self.center_box)

        self.global_inventory()
        pygame.draw.rect(self.screen, (133, 0, 133), self.preview_rect)
        # Draw preview sprite

        pygame.draw.rect(self.screen, (133, 0, 133), self.weapon_rect)
        if self.weapon_equipped:
            self.screen.blit(pygame.transform.scale(str_2_item(self.weapon_equipped[0], self.weapon_equipped[1], self.weapon_equipped[2], self.weapon_equipped[3]).sprite, (self.weapon_rect[2], self.weapon_rect[3])), (self.weapon_rect[0], self.weapon_rect[1]))
        else:
            self.screen.blit(self.weapon_placeholder, (self.weapon_rect[0], self.weapon_rect[1]))

        pygame.draw.rect(self.screen, (133, 0, 133), self.helmet_rect)
        if self.helmet_equipped:
            self.screen.blit(pygame.transform.scale(str_2_item(self.helmet_equipped[0], self.helmet_equipped[1], self.helmet_equipped[2], self.helmet_equipped[3]).sprite, (self.helmet_rect[2], self.helmet_rect[3])), (self.helmet_rect[0], self.helmet_rect[1]))
        else:
            self.screen.blit(self.helmet_placeholder, (self.helmet_rect[0], self.helmet_rect[1]))

        pygame.draw.rect(self.screen, (133, 0, 133), self.chestplate_rect)
        if self.chestplate_equipped:
            self.screen.blit(pygame.transform.scale(str_2_item(self.chestplate_equipped[0], self.chestplate_equipped[1], self.chestplate_equipped[2], self.chestplate_equipped[3]).sprite, (self.chestplate_rect[2], self.chestplate_rect[3])), (self.chestplate_rect[0], self.chestplate_rect[1]))
        else:
            self.screen.blit(self.chestplate_placeholder, (self.chestplate_rect[0], self.chestplate_rect[1]))

        pygame.draw.rect(self.screen, (133, 0, 133), self.boots_rect)
        if self.boots_equipped:
            self.screen.blit(pygame.transform.scale(str_2_item(self.boots_equipped[0], self.boots_equipped[1], self.boots_equipped[2], self.boots_equipped[3]).sprite, (self.boots_rect[2], self.boots_rect[3])), (self.boots_rect[0], self.boots_rect[1]))
        else:
            self.screen.blit(self.boots_placeholder, (self.boots_rect[0], self.boots_rect[1]))

        # Item hover
        for i in range(self.length**2):
            # self.length**2 * self.page
            mx, my = pygame.mouse.get_pos()
            if mx >= self.inventory_rect[0] and mx <= self.inventory_rect[0] + self.inventory_rect[2] and my >= self.inventory_rect[1] and my <= self.inventory_rect[1] + self.inventory_rect[3]:
                if mx >= self.grid[i][0] and mx <= self.grid[i][0] + self.grid[i][2] and my >= self.grid[i][1] and my <= self.grid[i][1] + self.grid[i][3]:
                    pygame.draw.rect(self.screen, (255, 255, 255), (self.inventory_rect[0] + self.inventory_rect[3] + self.button_page_up.rect[2] + 2, self.inventory_rect[1] + self.inventory_rect[3]/2 - 50/2, 200, 50))
