import pygame
import time
from game.game import Game
from player.player import Player
import convert.convert as convert

class Training(Game):

    def __init__(self):
        super().__init__()

        w = int(self.screen.get_width()/1.7)
        h = convert.scale_h([5504, 3808], w)
        x = int(self.screen.get_width()/2 - w/2)
        y = int(self.screen.get_height()/2 - h/2)
        self.platform_rect = [x, y, w, h]

        self.player = Player(self.screen, [self.platform_rect[0], self.platform_rect[1], 25, 25], self.platform_rect, 150)

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

    def update(self):
        super().update()
        self.player.update(self.dt)

    def draw(self):
        super().draw()
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 150, 0), self.platform_rect)
        self.player.draw()
