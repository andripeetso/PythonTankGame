# main.py

import pygame
import sys
from tank import Tank
from projectile import Projectile
from terrain import Terrain
from utils import load_image, collide_rect, distance

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tank Game")

# Load assets
tank_image = 'assets/images/tank.png'
projectile_image = 'assets/images/projectile.png'
terrain_image = 'assets/images/terrain.png'

# Create game objects
player_tank = Tank(400, 300, tank_image, 5, 3)
terrain = Terrain(0, 0, 800, 600, terrain_image)
projectiles = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_tank.move_forward()
            elif event.key == pygame.K_DOWN:
                player_tank.move_backward()
            elif event.key == pygame.K_LEFT:
                player_tank.rotate_left()
            elif event.key == pygame.K_RIGHT:
                player_tank.rotate_right()
            elif event.key == pygame.K_SPACE:
                # Fire a projectile
                x, y = player_tank.x, player_tank.y
                angle = player_tank.angle
                projectiles.append(Projectile(x, y, angle, 10, projectile_image))

    # Update the position of the projectiles
    for projectile in projectiles:
        projectile.move()
        # Remove projectiles that are out of bounds
        if projectile.out_of_bounds(800, 600):
            projectiles.remove(projectile)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the terrain
    terrain.draw(screen)

    # Draw the tank
    player_tank.draw(screen)

    # Draw the projectiles
    for projectile in projectiles:
        projectile.draw(screen)

    # Update the display
    pygame.display.update()
