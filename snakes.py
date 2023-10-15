# Import necessary libraries
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Constants for the game
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize Snake variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_dir = (0, 1)
snake_speed = 1  # Adjust this value to control the snake's speed

# Initialize Food variables
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Game over flag
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            # Handle arrow key inputs to change the snake's direction
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

    # Move the snake by adding a new head position
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check for collisions with the food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()  # Remove the last segment to simulate movement

    # Check if the snake hits the wall
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
    ):
        game_over = True

    # Check if the snake hits itself
    if snake[0] in snake[1:]:
        game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
        )

    # Draw the food
    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Update the display
    pygame.display.update()

    # Control the snake's speed by setting the game's frame rate
    pygame.time.Clock().tick(snake_speed)

# Quit Pygame after the game loop
pygame.quit()
