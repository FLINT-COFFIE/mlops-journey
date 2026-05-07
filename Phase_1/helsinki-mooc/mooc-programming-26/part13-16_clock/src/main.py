# write your solution here
import pygame
import math
from datetime import datetime

# Initialize Pygame
pygame.init()

# Setup display
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog System Clock")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 150)

# Clock settings
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 250
CLOCK_CLOCK = pygame.time.Clock()


def get_hand_position(angle, length):
    """Calculates the end point of a clock hand based on angle and length."""
    # Subtracting 90 degrees (pi/2) because 0 degrees in math starts at 3 o'clock
    x = CENTER[0] + length * math.cos(math.radians(angle - 90))
    y = CENTER[1] + length * math.sin(math.radians(angle - 90))
    return x, y


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Get current system time
    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # 2. Calculate angles (360 degrees / units)
    # Hour hand: 30 deg per hour + offset for minutes
    hour_angle = (hour * 30) + (minute * 0.5)
    # Minute hand: 6 deg per minute
    minute_angle = minute * 6
    # Second hand: 6 deg per second
    second_angle = second * 6

    # 3. Draw everything
    screen.fill(WHITE)

    # Draw clock face
    pygame.draw.circle(screen, BLACK, CENTER, RADIUS, 4)
    pygame.draw.circle(screen, BLACK, CENTER, 10)  # Center pin

    # Draw hour markers (simple lines)
    for i in range(12):
        angle = i * 30
        p1 = get_hand_position(angle, RADIUS - 10)
        p2 = get_hand_position(angle, RADIUS)
        pygame.draw.line(screen, BLACK, p1, p2, 4)

    # Draw hands (Hour = Short/Thick, Minute = Long, Second = Red/Thin)
    pygame.draw.line(
        screen, BLACK, CENTER, get_hand_position(hour_angle, RADIUS * 0.5), 8
    )
    pygame.draw.line(
        screen, BLUE, CENTER, get_hand_position(minute_angle, RADIUS * 0.8), 5
    )
    pygame.draw.line(
        screen, RED, CENTER, get_hand_position(second_angle, RADIUS * 0.9), 2
    )

    pygame.display.flip()
    CLOCK_CLOCK.tick(60)

pygame.quit()
