import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodging Obstacles Game")

clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GOLD_COLOR = (212, 175, 55)

# Highscore file
HIGH_SCORE_FILE = "highscore.txt"
if os.path.exists(HIGH_SCORE_FILE):
    with open(HIGH_SCORE_FILE, "r") as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0
else:
    highscore = 0

# Define the Player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.centery = HEIGHT // 2
        self.speed = 5
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep the player within screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Define the Obstacle sprite
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = random.randint(20, 50)
        self.height = random.randint(20, 50)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(0, 100)
        self.rect.y = random.randint(0, HEIGHT - self.height)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

# Define the Gold collectible sprite
class Gold(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10
        # Create a surface with per-pixel alpha for a transparent background
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GOLD_COLOR, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH + random.randint(0, 100)
        self.rect.y = random.randint(0, HEIGHT - self.radius * 2)
        self.speed = 4

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()

# Sprite groups
player_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
gold_group = pygame.sprite.Group()

player = Player()
player_group.add(player)

# Game variables
score = 0  # Gold collected in the current round
obstacle_spawn_delay = 1500  # milliseconds between obstacle spawns
gold_spawn_delay = 3000      # milliseconds between gold spawns

last_obstacle_spawn = pygame.time.get_ticks()
last_gold_spawn = pygame.time.get_ticks()

game_over = False

font = pygame.font.SysFont(None, 36)

# Main game loop
running = True
while running:
    clock.tick(60)  # Run at 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        now = pygame.time.get_ticks()

        # Spawn obstacles periodically
        if now - last_obstacle_spawn > obstacle_spawn_delay:
            last_obstacle_spawn = now
            obstacle = Obstacle()
            obstacle_group.add(obstacle)

        # Spawn gold periodically
        if now - last_gold_spawn > gold_spawn_delay:
            last_gold_spawn = now
            gold = Gold()
            gold_group.add(gold)

        # Update all sprites
        player_group.update()
        obstacle_group.update()
        gold_group.update()

        # Check collision with obstacles
        hits = pygame.sprite.spritecollide(player, obstacle_group, True)
        if hits:
            player.lives -= 1
            if player.lives <= 0:
                game_over = True

        # Check collision with gold
        gold_hits = pygame.sprite.spritecollide(player, gold_group, True)
        if gold_hits:
            score += len(gold_hits)

    # Drawing section
    screen.fill(BLACK)
    player_group.draw(screen)
    obstacle_group.draw(screen)
    gold_group.draw(screen)

    # Display current score, lives, and highscore
    score_text = font.render(f"Gold: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {player.lives}", True, WHITE)
    highscore_text = font.render(f"Highscore: {highscore}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))
    screen.blit(highscore_text, (10, 70))

    # Game over screen
    if game_over:
        over_text = font.render("GAME OVER! Press R to Restart or Q to Quit.", True, WHITE)
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset game variables to restart
            game_over = False
            player.lives = 3
            score = 0
            obstacle_group.empty()
            gold_group.empty()
            player.rect.centery = HEIGHT // 2
        elif keys[pygame.K_q]:
            running = False

    pygame.display.flip()

# Save new highscore if the current score beats it
if score > highscore:
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

pygame.quit()
sys.exit()
