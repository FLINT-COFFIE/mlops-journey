# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

x_max = 640 - width
y_max = 480 - height

#starting
x = random.randint(0, x_max)
y = random.randint(0, y_max)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        
        if mouse_x >= x and mouse_x <= x + width:
            if mouse_y >= y and mouse_y <= y + height:
                    # teleport
                    x = random.randint(0, x_max)
                    y = random.randint(0, y_max)
                    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    clock.tick(60)