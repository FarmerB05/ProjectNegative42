import pygame
import time
from button import Button

class SelectCarousel:

    def __init__(self, screen, rect, selections=None, background=False, background_color=None, font_size=25, font='chalkduster.ttf', font_color=None):
        self.screen = screen
        self.rect = rect
        self.counter = 0
        self.background = background

        if selections is None:
            self.selections = []
        else:
            self.selections = selections

        if font_color is None:
            self.font_color = (0, 0, 0)
        else:
            self.font_color = font_color

        if background_color is None:
            self.background_color = (255, 255, 255)
        else:
            self.background_color = background_color

        # Buttons
        self.backward_button = Button('<', [self.rect[0] - self.rect[3], self.rect[1], self.rect[3], self.rect[3]], self.screen)
        self.forward_button = Button('>', [self.rect[0] + self.rect[2], self.rect[1], self.rect[3], self.rect[3]], self.screen)

        # text
        pygame.font.init()
        self.font = pygame.font.SysFont(font, font_size)
        self.font_text = self.font.render(self.selections[0], True, self.font_color)

        # timer
        self.cooldown = time.time() + 0.2

    def get_selected(self):
        return self.selections[self.counter]

    def update(self):
        self.forward_button.update()
        self.backward_button.update()

        if time.time() >= self.cooldown:
            if self.forward_button.click():
                if self.counter >= len(self.selections) - 1:
                    self.counter = 0
                else:
                    self.counter += 1
                self.font_text = self.font.render(self.selections[self.counter], True, self.font_color)
                self.cooldown = time.time() + 0.2

            if self.backward_button.click():
                if self.counter <= 0:
                    self.counter = len(self.selections) - 1
                else:
                    self.counter -= 1

                self.font_text = self.font.render(self.selections[self.counter], True, self.font_color)
                self.cooldown = time.time() + 0.2

    def draw(self):
        if self.background:
            pygame.draw.rect(self.screen, self.background_color, self.rect) # background

        self.forward_button.draw()
        self.backward_button.draw()

        text_rect = (self.font_text.get_width(), self.font_text.get_height())
        self.screen.blit(self.font_text, (self.rect[0] + self.rect[2]/2 - text_rect[0]/2, self.rect[1] + self.rect[3]/2 - text_rect[1]/2))
