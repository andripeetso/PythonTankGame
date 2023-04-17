import pygame
import sys
from tank import Tank
from projectile import Projectile
from terrain import Terrain
from utils import load_image

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((416, 416))
pygame.display.set_caption("Tank Game")

# Load assets
tank_image = 'assets/images/tank.png'
projectile_image = 'assets/images/projectile.png'
terrain_image = 'assets/images/terrain.png'

# Create game objects
player_tank = Tank(32 * 6, 32 * 12, tank_image)
terrain = Terrain(0, 0, 416, 416, terrain_image)
projectiles = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_tank.move(270)
            elif event.key == pygame.K_DOWN:
                player_tank.move(90)
            elif event.key == pygame.K_LEFT:
                player_tank.move(180)
            elif event.key == pygame.K_RIGHT:
                player_tank.move(0)
            elif event.key == pygame.K_SPACE:
                if player_tank.can_fire():
                    x, y = player_tank.x, player_tank.y
                    angle = player_tank.angle
                    projectiles.append(Projectile(x, y, angle, 10, projectile_image))

    # Update the position of the projectiles
    for projectile in projectiles:
        projectile.move()
        # Remove projectiles that are out of bounds
        if projectile.out_of_bounds(416, 416):
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
