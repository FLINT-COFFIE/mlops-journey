# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

width = ball.get_width()
height = ball.get_height()

x = 320
y = 240

vx = 2
vy = 2



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            

    x += vx
    y += vy
    
    if x <= 0 or x >= 640 - width:
        vx = -vx
        
    if y <= 0 or y >= 480 - height:
        vy = -vy
        
    window.fill((0, 0, 0))
        
    window.blit(ball, (x, y))

    pygame.display.flip()

    clock.tick(60)