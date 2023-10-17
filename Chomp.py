# Example file showing a basic pygame "game loop"
import pygame

HEIGHT = 500
WIDTH = 600
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
running = True

rect_height = 100
background = pygame.Surface((WIDTH,HEIGHT))
background.fill((47, 139, 237))
pygame.draw.rect(background, (255, 231, 143),(0,HEIGHT-rect_height,WIDTH,rect_height))
screen.blit(background,(0,0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()