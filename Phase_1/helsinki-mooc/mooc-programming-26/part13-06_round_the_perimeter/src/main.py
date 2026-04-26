import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

width = robot.get_width()
height = robot.get_height()

max_x = 640 - width
max_y = 480 - height

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
    
   
    if y <= 0 and x < max_x:
        x += velocity
        
    
    elif x >= max_x and y < max_y:
        y += velocity
        
    
    elif y >= max_y and x > 0:
        x -= velocity
        
    elif x <= 0 and y > 0:
        y -= velocity
    
    clock.tick(60)