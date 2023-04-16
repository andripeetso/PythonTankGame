# terrain.py

import pygame

class Terrain:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert()

    def draw(self, screen):
        for i in range(0, self.width, self.image.get_width()):
            for j in range(0, self.height, self.image.get_height()):
                screen.blit(self.image, (i, j))
