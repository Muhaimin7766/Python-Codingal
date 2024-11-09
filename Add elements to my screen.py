import pygame
import sys

pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Add Elements to Screen")

white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

font = pygame.font.Font(None, 36)

text = font.render("Hello, Pygame!", True, red)
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    pygame.draw.rect(screen, green, (screen_width // 2 - 50, screen_height // 2, 100, 50))

    screen.blit(text, text_rect)

    
    pygame.display.flip()

pygame.quit()
