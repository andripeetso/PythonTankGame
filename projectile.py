# projectile.py

import pygame
import math

class Projectile:
    def __init__(self, x, y, angle, speed, image):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.image = pygame.image.load(image).convert_alpha()
        self.active = True

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        screen.blit(rotated_image, rect.topleft)

    def move(self):
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

    def out_of_bounds(self, width, height):
        if self.x < 0 or self.x > width or self.y < 0 or self.y > height:
            self.active = False
            
    def get_rect(self):
        return self.image.get_rect(center=(self.x, self.y))
