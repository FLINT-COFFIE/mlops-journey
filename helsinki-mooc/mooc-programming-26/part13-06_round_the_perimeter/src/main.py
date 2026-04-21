import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

# Pre-calculate the furthest the robot can go
max_x = 640 - width
max_y = 480 - height

# Start position: Top-Right
x = max_x
y = 0

velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    # 1. TOP EDGE: Move right if there is room
    if y <= 0 and x < max_x:
        x += velocity
        
    # 2. RIGHT EDGE: Move down if at the right wall
    elif x >= max_x and y < max_y:
        y += velocity
        
    # 3. BOTTOM EDGE: Move left if at the floor
    elif y >= max_y and x > 0:
        x -= velocity
        
    # 4. LEFT EDGE: Move up if at the left wall
    elif x <= 0 and y > 0:
        y -= velocity
    
    clock.tick(60)