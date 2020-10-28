import pygame

class Button:

    def __init__(self, text, rect, screen, colors=None, images=None, text_color=None, font_size=25, font='chalkduster.ttf'):
        self.text = text
        self.rect = rect # [x, y, w, h]
        self.screen = screen

        # colors : [default, hover]
        if colors is None:
            self.colors = [(255, 255, 255), (100, 100, 100)]
        else:
            self.colors = colors

        # images : [default, hover], just filepath
        if images is None:
            self.images = [None, None]
        else:
            if self.images[0] and self.images[1]: # Images
                self.images[0] = pygame.transform.scale(pygame.image.load(self.images[0]).convert(), (rect[2], rect[3]))
                self.images[1] = pygame.transform.scale(pygame.image.load(self.images[1]).convert(), (rect[2], rect[3]))
            else:
                self.images = [None, None]

        # text_color
        if text_color is None:
            self.text_color = (0, 0, 0)
        else:
            self.text_color = text_color

        # Text
        pygame.font.init()
        self.font = pygame.font.SysFont(font, font_size)
        self.font_text = self.font.render(self.text, True, self.text_color)

    def hover(self):
        mx, my = pygame.mouse.get_pos()
        if mx >= self.rect[0] and mx <= self.rect[0] + self.rect[2] and my >= self.rect[1] and my <= self.rect[1] + self.rect[3]:
            return True
        else:
            return False

    def click(self):
        if pygame.mouse.get_pressed()[0]:
            if self.hover():
                return True
        else:
            return False

    def update(self):
        pass

    def draw(self):
        # Button background
        if self.images[0] and self.images[1]:
            if self.hover():
                self.screen.blit(self.images[1], (self.rect[0], self.rect[1]))
            else:
                self.screen.blit(self.images[0], (self.rect[0], self.rect[1]))
        else:
            if self.hover():
                pygame.draw.rect(self.screen, self.colors[1], self.rect)
            else:
                pygame.draw.rect(self.screen, self.colors[0], self.rect)

        # Button text
        text_rect = (self.font_text.get_width(), self.font_text.get_height())
        self.screen.blit(self.font_text, (self.rect[0] + self.rect[2]/2 - text_rect[0]/2, self.rect[1] + self.rect[3]/2 - text_rect[1]/2))
