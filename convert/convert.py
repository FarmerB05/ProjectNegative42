import pygame
from item.sword import Sword

def scale_h(rect, w):
    # rect = [w, h]
    return int((rect[1]/rect[0]) * w)

def scale_w(rect, h):
    return int((rect[0]/rect[1]) * h)

def str_2_item(str, level):
    if str == 'sword':
        return Sword(pygame.image.load('sword.png'))
    return None

def str_2_key(str):
    if str == 'space':
        return pygame.K_SPACE
    elif str == 'a':
        return pygame.K_a
    elif str == 'b':
        return pygame.K_b
    elif str == 'c':
        return pygame.K_c
    elif str == 'd':
        return pygame.K_d
    elif str == 'e':
        return pygame.K_e
    elif str == 'f':
        return pygame.K_f
    elif str == 'g':
        return pygame.K_g
    elif str == 'h':
        return pygame.K_h
    elif str == 'i':
        return pygame.K_i
    elif str == 'j':
        return pygame.K_j
    elif str == 'k':
        return pygame.K_k
    elif str == 'l':
        return pygame.K_l
    elif str == 'm':
        return pygame.K_m
    elif str == 'n':
        return pygame.K_n
    elif str == 'o':
        return pygame.K_o
    elif str == 'p':
        return pygame.K_p
    elif str == 'q':
        return pygame.K_q
    elif str == 'r':
        return pygame.K_r
    elif str == 's':
        return pygame.K_s
    elif str == 't':
        return pygame.K_t
    elif str == 'u':
        return pygame.K_u
    elif str == 'v':
        return pygame.K_v
    elif str == 'w':
        return pygame.K_w
    elif str == 'x':
        return pygame.K_x
    elif str == 'y':
        return pygame.K_y
    elif str == 'z':
        return pygame.K_z

    return None
