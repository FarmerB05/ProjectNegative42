import pygame
import time
from game.game import Game

class Training(Game):

    def __init__(self):
        super().__init__()

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
            self.video_event(event)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
        self.screen.fill((255, 255, 255))
