import pygame
import time
from game.game import Game
from player.player import Player
import convert.convert as convert
from inventory.inventory import Inventory
from inventory.inventory_display import InventoryDisplay
from gui.button import Button
from convert.convert import str_2_key

class Training(Game):

    def __init__(self):
        super().__init__()

        w = int(self.screen.get_width()/1.7)
        h = convert.scale_h([5504, 3808], w)
        x = int(self.screen.get_width()/2 - w/2)
        y = int(self.screen.get_height()/2 - h/2)
        self.platform_rect = [x, y, w, h]

        self.player = Player(self.screen, [self.platform_rect[0], self.platform_rect[1], 25, 25], self.platform_rect, 150, name='player', save_entity=False)

        self.inventory = Inventory()
        self.inventory_display = InventoryDisplay(self.screen, [self.player])
        self.inventory_open = False

    def run(self):
        while self.running:
            self.event_loop()
            self.update()
            self.draw()
            self.dt = self.clock.tick(self.fps) / 1000
            pygame.display.flip()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.video_event(event):
                # Scale
                self.platform_rect = [int(self.screen.get_width()/2 - int(self.screen.get_width()/1.7)/2), int(self.screen.get_height()/2 - convert.scale_h([5504, 3808], int(self.screen.get_width()/1.7))/2), int(self.screen.get_width()/1.7), convert.scale_h([5504, 3808], int(self.screen.get_width()/1.7))]
                self.player.scale(self.last_screen, self.platform_rect)
                self.inventory_display.scale()

            if event.type == pygame.KEYDOWN:
                if event.key == str_2_key('e'):
                    self.inventory_open = not self.inventory_open

    def update(self):
        super().update()
        self.player.update(self.dt)

    def draw(self):
        super().draw()
        if not self.inventory_open:
            pygame.draw.rect(self.screen, (0, 150, 0), self.platform_rect)
            self.player.draw()

        if self.inventory_open:
            self.inventory_display.update()
            self.inventory_display.draw()
