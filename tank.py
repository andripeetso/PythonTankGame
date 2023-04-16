# tank.py

import pygame
import math

class Tank:
    def __init__(self, x, y, image, rotation_speed, move_speed):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.rotation_speed = rotation_speed
        self.move_speed = move_speed
        self.angle = 0

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        screen.blit(rotated_image, rect.topleft)

    def move_forward(self):
        self.x += self.move_speed * math.cos(math.radians(self.angle))
        self.y -= self.move_speed * math.sin(math.radians(self.angle))

    def move_backward(self):
        self.x -= self.move_speed * math.cos(math.radians(self.angle))
        self.y += self.move_speed * math.sin(math.radians(self.angle))

    def rotate_left(self):
        self.angle += self.rotation_speed

    def rotate_right(self):
        self.angle -= self.rotation_speed
