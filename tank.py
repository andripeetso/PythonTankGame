import pygame
import math
import random
from utils import load_image

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.original_image = load_image(image)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (x, y)
        self.angle = 270

    def move(self, angle):
        self.angle = angle
        if self.angle == 270:
            new_y = self.y - 32
            if new_y >= 0:
                self.y = new_y
        elif self.angle == 90:
            new_y = self.y + 32
            if new_y <= 384:
                self.y = new_y
        elif self.angle == 180:
            new_x = self.x - 32
            if new_x >= 0:
                self.x = new_x
        elif self.angle == 0:
            new_x = self.x + 32
            if new_x <= 384:
                self.x = new_x

        self.update_image()

    def update_image(self):
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def can_fire(self):
        return True