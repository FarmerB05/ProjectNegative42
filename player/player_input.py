import pygame
import time
from convert.convert import str_2_key

class PlayerInput:

    def __init__(self, boundry, speed):
        self.boundry = boundry
        self.speed = speed
        self.x_vel = 0
        self.y_vel = 0

        self.dodge_timer = time.time() + 1

    def movement(self, rect, settings, dt):
        self.x_vel = 0
        self.y_vel = 0
        keys = pygame.key.get_pressed()

        if rect[1] > self.boundry[1]:
            if keys[str_2_key(settings.controls['up'])]: # up
                self.y_vel -= self.speed * dt

        if rect[0] > self.boundry[0]:
            if keys[str_2_key(settings.controls['left'])]: # left
                self.x_vel -= self.speed * dt

        if rect[1] + rect[3] < self.boundry[1] + self.boundry[3]:
            if keys[str_2_key(settings.controls['down'])]: # down
                self.y_vel += self.speed * dt

        if rect[0] + rect[2] < self.boundry[0] + self.boundry[2]:
            if keys[str_2_key(settings.controls['right'])]: # right
                self.x_vel += self.speed * dt

        # Dodge
        if time.time() >= self.dodge_timer:
            if keys[str_2_key(settings.controls['dodge'])]: # right
                tmp_x = 0
                tmp_y = 0

                if keys[str_2_key(settings.controls['up'])]: # up
                    if rect[1] - int(self.speed // 2.5) > self.boundry[1]:
                            tmp_y -= int(self.speed // 2.5)
                    else:
                        rect[1] = self.boundry[1]

                if keys[str_2_key(settings.controls['left'])]: # left
                    if rect[0] - int(self.speed // 2.5) > self.boundry[0]:
                            tmp_x -= int(self.speed // 2.5)
                    else:
                        rect[0] = self.boundry[0]

                if keys[str_2_key(settings.controls['down'])]: # down
                    if rect[1] + rect[3] + int(self.speed // 2.5) < self.boundry[1] + self.boundry[3]:
                        tmp_y += int(self.speed // 2.5)
                    else:
                        rect[1] = self.boundry[1] + self.boundry[3] - rect[3]

                if keys[str_2_key(settings.controls['right'])]: # right
                    if rect[0] + rect[2] + int(self.speed // 2.5) < self.boundry[0] + self.boundry[2]:
                        tmp_x += int(self.speed // 2.5)
                    else:
                        rect[0] = self.boundry[0] + self.boundry[2] - rect[2]

                if not tmp_x == 0 and not tmp_y == 0:
                    # 0.7071 is the ratio of the side lengths. So the opposite is about 0.7071 times as long as the Hypotenuse.
                    tmp_x *= 0.7071
                    tmp_y *= 0.7071

                rect[0] += tmp_x
                rect[1] += tmp_y

                self.dodge_timer = time.time() + 1

        if not self.x_vel == 0 and not self.y_vel == 0:
            # 0.7071 is the ratio of the side lengths. So the opposite is about 0.7071 times as long as the Hypotenuse.
            self.x_vel *= 0.7071
            self.y_vel *= 0.7071

        rect[0] += self.x_vel
        rect[1] += self.y_vel

        return rect[0], rect[1]

    def update_position(self, rect, settings, dt):
        rect[0], rect[1] = self.movement(rect, settings, dt)
        return rect[0], rect[1]
