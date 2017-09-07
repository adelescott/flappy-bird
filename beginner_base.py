# Task 0.2 Import pygame
import pygame
pygame.init()

# Task 3.3 Random pipe sizes
import random

# Task 4.3 Close the game
import sys

# Task 1.1 Displaying the screen
size_x = 800
size_y = 600
size = (size_x, size_y)
screen = pygame.display.set_mode(size)

# Task 1.2 Displaying the background
background_image = pygame.image.load("bg.png")
background_x = 0
background_y = 0
screen.blit(background_image, (background_x, background_y))
pygame.display.update()

# Task 2.1 Flappy bird
bird_image = pygame.image.load("bird.png")
bird_x = 200
bird_y = 300
screen.blit(bird_image, (bird_x, bird_y))
pygame.display.update()

# Task 3.1 Create a list of pipes
pipe_image = pygame.image.load("pipe.png")
pipe_x_positions = [500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300]
pipes = []
for pipe_x_position in pipe_x_positions:
    new_pipe = {}
    new_pipe['x'] = pipe_x_position
    new_pipe['y'] = 500
    pipes.append(new_pipe)

    # Task 3.3 Random pipe sizes
    new_pipe['y'] = random.randint(250, 500)

    # Bonus 3.5 Flip the pipe
    new_pipe['flipped'] = random.randint(0, 1)
    if new_pipe['flipped']:
        new_pipe['y'] = size_y - new_pipe['y'] - pipe_image.get_rect().size[1]

# Task 2.2 Create the game loop
game_running = True
moving = ""

while game_running:    
    pygame.display.update()
    
    # Task 2.3 Capturing events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                moving = "down"
            elif event.key == pygame.K_UP:
                moving = "up"
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or pygame.K_UP:
                moving = ""
    print(moving)

    # Task 2.4 Updating the bird's position
    if moving == "up":
        bird_y = bird_y - 1
    elif moving == "down":
        bird_y = bird_y + 1

    # Task 2.5 Reducing trailing
    screen.blit(background_image, (background_x, background_y))    
    screen.blit(bird_image, (bird_x, bird_y))

    # Task 3.2 Draw the pipes
    for pipe in pipes:
        # Bonus 3.5 Flip the pipe
        if pipe['flipped']: 
            flipped_pipe_image = pygame.transform.flip(pipe_image, False, True)
            screen.blit(flipped_pipe_image, (pipe['x'], pipe['y']))
        else:
            screen.blit(pipe_image, (pipe['x'], pipe['y']))
        # Task 3.4 Make the pipes move
        pipe['x'] = pipe['x'] - 1

        # Task 4.1 Detect a collision
        pipe_rect = pipe_image.get_rect().move(pipe['x'], pipe['y'])
        bird_rect = bird_image.get_rect().move(bird_x, bird_y)
        collision = pipe_rect.colliderect(bird_rect)
        if collision:
            print("Oh no, you lose.")
            # Task 4.2 Stop the game
            game_running = False

# Bonus 4.3 Close the game
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.display.quit()
            sys.exit()
