import pygame
import time
from game.game import Game
from player.player import Player

class Training(Game):

    def __init__(self):
        super().__init__()
        self.player = Player(self.screen, [20, 20, 25, 25], [0, 0, self.screen.get_width(), self.screen.get_height()], 150)

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
                self.player.scale()

    def update(self):
        super().update()
        self.player.update(self.dt)

    def draw(self):
        super().draw()
        self.screen.fill((255, 255, 255))
        self.player.draw()
