import pygame

class InputField:

    def __init__(self, screen, rect, placeholder='', margin=2, fill=False, background_color=None, text_color=None, font_size=25):
        self.screen = screen
        self.rect = rect
        self.placeholder = placeholder
        self.margin = margin
        self.fill = False

        # Background color
        if background_color is None:
            self.background_color = (255, 255, 255)
        else:
            self.background_color = background_color

        # text_color 
        if text_color is None:
            self.text_color = (0, 0, 0)
        else:
            self.text_color = text_color

        self.text = ''
        self.focused = False

        # Font
        self.range = -9
        self.font = pygame.font.SysFont('chalkduster.ttf', font_size)
        self.font_text = self.font.render(self.text, True, self.text_color)
        self.font_placeholder = self.font.render(self.placeholder, True, self.text_color)

    def focus(self):
        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            if mx >= self.rect[0] and mx <= self.rect[0] + self.rect[2] and my >= self.rect[1] and my <= self.rect[1] + self.rect[3]:
                self.focused = True
            else:
                self.focused = False

    def update(self, event): # Call in main event loop
        if self.focused:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

        # Text update
        self.font_text = self.font.render(self.text[self.range:], True, self.text_color)
        self.placeholder_text = self.font.render(self.placeholder[self.range:], True, self.text_color)

    def draw(self):
        self.focus()
        # Box
        if self.fill:
            pygame.draw.rect(self.screen, self.background_color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.background_color, self.rect, 1)

        # Text
        if not self.text: # Placeholder
            # Draw placeholder
            placeholder_rect = (self.font_placeholder.get_width(), self.font_placeholder.get_height())
            self.screen.blit(self.font_placeholder, (self.rect[0] + self.margin, self.rect[1] + self.rect[3]/2 - placeholder_rect[1]/2))
        else: # input_text
            text_rect = (self.font_text.get_width(), self.font_text.get_height())
            self.screen.blit(self.font_text, (self.rect[0] + self.margin, self.rect[1] + self.rect[3]/2 - text_rect[1]/2))
