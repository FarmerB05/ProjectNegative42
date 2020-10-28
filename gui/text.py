import pygame

class Text:

    def __init__(self, screen, text, rect, underline=False, font='chalkduster.ttf', font_size=25, font_color=None):
        self.screen = screen
        self.text = text
        self.rect = rect
        self.font = font
        self.font_size = font_size

        if font_color is None:
            self.font_color = (255, 255, 255)
        else:
            self.font_color = font_color

        # text
        pygame.font.init()
        self.font = pygame.font.SysFont(self.font, self.font_size)

        if underline:
            self.font.set_underline(True)

        self.font_text = self.font.render(str(self.text), True, self.font_color)

    def update(self):
        self.font_text = self.font.render(str(self.text), True, self.font_color)

    def draw(self):
        text_rect = (self.font_text.get_width(), self.font_text.get_height())
        self.screen.blit(self.font_text, (self.rect[0] + self.rect[2]/2 - text_rect[0]/2, self.rect[1] + self.rect[3]/2 - text_rect[1]/2))
