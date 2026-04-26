# Complete your game here
import pygame
import random

def init_game():
    pygame.init()
    window = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Sensor Guardian: Data Collection")
    
    # Loading images
    images = {
        "robot": pygame.image.load("robot.png"),
        "coin": pygame.image.load("coin.png"),
        "monster": pygame.image.load("monster.png")
    }
    
    return window, images

#monster spawn
def get_random_pos(img_width, img_height):
    x = random.randint(0, 640 - img_width)
    y = random.randint(0, 480 - img_height)
    return x, y

#collition 
def check_collision(obj1_pos, obj1_img, obj2_pos, obj2_img):
    # Returns True if two sprites overlap
    rect1 = pygame.Rect(obj1_pos[0], obj1_pos[1], obj1_img.get_width(), obj1_img.get_height())
    rect2 = pygame.Rect(obj2_pos[0], obj2_pos[1], obj2_img.get_width(), obj2_img.get_height())
    return rect1.colliderect(rect2)

def run_game():
    window, assets = init_game()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    # object locations
    robot_x, robot_y = 320, 400
    coin_x, coin_y = get_random_pos(assets["coin"].get_width(), assets["coin"].get_height())
    
    # Monster setup (List of dicts for scaling)
    monsters = []
    for i in range(3):
        mx, my = get_random_pos(assets["monster"].get_width(), assets["monster"].get_height())
        monsters.append({"x": mx, "y": my, "vx": random.choice([-2, 2]), "vy": random.choice([-2, 2])})

    score = 0
    game_over = False

    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if not game_over:
            # Player Control
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and robot_x > 0: robot_x -= 5
            if keys[pygame.K_RIGHT] and robot_x < 640 - assets["robot"].get_width(): robot_x += 5
            if keys[pygame.K_UP] and robot_y > 0: robot_y -= 5
            if keys[pygame.K_DOWN] and robot_y < 480 - assets["robot"].get_height(): robot_y += 5

            # Coin Collection
            if check_collision((robot_x, robot_y), assets["robot"], (coin_x, coin_y), assets["coin"]):
                score += 1
                coin_x, coin_y = get_random_pos(assets["coin"].get_width(), assets["coin"].get_height())

            # Monster Movement & Collision
            for m in monsters:
                m["x"] += m["vx"]
                m["y"] += m["vy"]
                
                # Bounce monsters off walls
                if m["x"] <= 0 or m["x"] >= 640 - assets["monster"].get_width(): m["vx"] *= -1
                if m["y"] <= 0 or m["y"] >= 480 - assets["monster"].get_height(): m["vy"] *= -1

                if check_collision((robot_x, robot_y), assets["robot"], (m["x"], m["y"]), assets["monster"]):
                    game_over = True

        window.fill((30, 30, 30)) # Dark Grey Background
        
        window.blit(assets["robot"], (robot_x, robot_y))
        window.blit(assets["coin"], (coin_x, coin_y))
        for m in monsters:
            window.blit(assets["monster"], (m["x"], m["y"]))

        # Score Counter
        score_text = font.render(f"Data Collected: {score}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))

        if game_over:
            msg = font.render("GAME OVER", True, (255, 0, 0))
            window.blit(msg, (180, 240))
            if keys[pygame.K_ESCAPE]: return

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_game()