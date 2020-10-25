import pygame
import time
from convert.convert import str_2_key

class PlayerInput:

    def __init__(self, boundry, speed):
        self.boundry = boundry
        self.speed = speed
        self.x_vel = 0
        self.y_vel = 0

    def movement(self, rect, settings, dt):
        keys = pygame.key.get_pressed()

        if rect[1] > self.boundry[1]:
            if keys[str_2_key(settings.controls['up'])]: # up
                self.y_vel -= self.speed * dt
    #    else:
    #s        rect[1] = self.boundry[1]

        if rect[0] > self.boundry[0]:
            if keys[str_2_key(settings.controls['left'])]: # left
                self.x_vel -= self.speed * dt
    #    else:
    #        rect[0] = self.boundry[0]

        if rect[1] + rect[3] < self.boundry[1] + self.boundry[3]:
            if keys[str_2_key(settings.controls['down'])]: # down
                self.y_vel += self.speed * dt
    #    else:
    #        rect[1] = self.boundry[1] + self.boundry[3]

        if rect[0] + rect[2] < self.boundry[0] + self.boundry[2]:
            if keys[str_2_key(settings.controls['right'])]: # right
                self.x_vel += self.speed * dt
    #    else:
        #    rect[0] = self.boundry[0] + self.boundry[2]

        return rect[0], rect[1]

    def update_position(self, rect, settings, dt):
        self.x_vel = 0
        self.y_vel = 0
        x, y = self.movement(rect, settings, dt)
        rect[0] += self.x_vel
        rect[1] += self.y_vel

        return rect[0], rect[1]
