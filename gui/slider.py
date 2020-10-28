import pygame
from button import Button
import time

class Slider:

    def __init__(self, screen, rect, pointer_width=10, value=0, max=100, background_color=None, pointer_color=None, font_size=25, font='chalkduster.ttf', font_color=None):
        self.screen = screen
        self.rect = rect
        self.value = value
        self.max = max

        self.pointer_rect = [self.rect[0] + (self.value * (self.rect[2] // self.max)), self.rect[1], pointer_width, self.rect[3]]

        self.rect[2] -= self.pointer_rect[2]

        if background_color is None:
            self.background_color = (255, 255, 255)
        else:
            self.background_color = background_color

        if pointer_color is None:
            self.pointer_color = (0, 0, 0)
        else:
            self.pointer_color = pointer_color

        if font_color is None:
            self.font_color = (0, 0, 0)
        else:
            self.font_color = font_color

        # Text
        pygame.font.init()
        self.font = pygame.font.SysFont(font, font_size)
        self.font_text = self.font.render(str(self.value), True, self.font_color)

    def update(self):
        self.font_text = self.font.render(str(self.value), True, self.font_color)

        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            if mx >= self.rect[0] and mx <= self.rect[0] + self.rect[2] and my >= self.rect[1] and my <= self.rect[1] + self.rect[3]:
                self.pointer_rect[0] = mx
                self.value = ((self.max * self.pointer_rect[0])-(self.max * self.rect[0])) // (self.rect[2])

    def draw(self):
        pygame.draw.rect(self.screen, self.background_color, (self.rect[0], self.rect[1], self.rect[2] + self.pointer_rect[2], self.rect[3]))
        pygame.draw.rect(self.screen, self.pointer_color, self.pointer_rect)

        # Text, Centered
        text_rect = (self.font_text.get_width(), self.font_text.get_height())
        self.screen.blit(self.font_text, (self.rect[0] + self.rect[2]/2 - text_rect[0]/2 + self.pointer_rect[2]/2, self.rect[1] + self.rect[3]/2 - text_rect[1]/2))
