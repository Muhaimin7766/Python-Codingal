import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Movement")

background_color = (255, 255, 255)  # White
sprite1_color = (0, 128, 0)  # Dark Green
sprite2_color = (255, 0, 0)  # Red

sprite1 = pygame.Rect(100, 100, 50, 50)
sprite2 = pygame.Rect(300, 300, 50, 50)
sprite_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite1.x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite1.x += sprite_speed
    if keys[pygame.K_UP]:
        sprite1.y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite1.y += sprite_speed

    screen.fill(background_color)

    pygame.draw.rect(screen, sprite1_color, sprite1)
    pygame.draw.rect(screen, sprite2_color, sprite2)

    pygame.display.flip()

pygame.quit()
