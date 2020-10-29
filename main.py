import pygame
import time
from settings.settings import Settings
from game.training import Training

if __name__ == '__main__':
    pygame.init()

    wow = Settings()
    wow.save()

    wow1 = Training()
    wow1.run()
