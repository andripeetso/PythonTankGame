# utils.py

import pygame

def load_image(image_path, transparent_color=None):
    image = pygame.image.load(image_path)
    if transparent_color is not None:
        image.set_colorkey(transparent_color)
    return image.convert()

def collide_rect(rect1, rect2):
    return rect1.colliderect(rect2)

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
