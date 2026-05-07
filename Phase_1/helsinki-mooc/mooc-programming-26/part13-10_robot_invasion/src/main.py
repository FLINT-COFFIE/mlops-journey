# WRITE YOUR SOLUTION HERE:
import pygame
import random

# Initialize Pygame
pygame.init()

# Setup display
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Robots - Helsinki MOOC Part 13")

# Load robot image
robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

# Clock to control frame rate
clock = pygame.time.Clock()

# List to store robot data: [x, y, velocity_x]
robots = []

# Timer for spawning robots
spawn_timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Clear screen
    window.fill((0, 0, 0))

    # Spawn a new robot randomly
    spawn_timer += 1
    # frequency
    if spawn_timer >= 30:
        start_x = random.randint(0, WIDTH - robot_width)
        start_y = -robot_height
        # velocity_x will be used once it hits the ground
        vel_x = random.choice([-2, 2])
        robots.append([start_x, start_y, vel_x])
        spawn_timer = 0

    # Update and draw robots
    for r in robots[:]:
        x, y, vx = r

        # Phase 1: Falling
        if y < HEIGHT - robot_height:
            r[1] += 2  # Falling speed
        # Phase 2: Walking
        else:
            r[0] += vx
            r[1] = HEIGHT - robot_height  # Stay on ground

        # Draw the robot
        window.blit(robot, (r[0], r[1]))

        # Remove robot if it goes off screen
        if r[0] < -robot_width or r[0] > WIDTH:
            robots.remove(r)

    pygame.display.flip()
    clock.tick(60)
