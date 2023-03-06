import pygame
pygame.init()
pygame.display.set_mode((1000,700))
pygame.display.set_caption("jeu1")

r = True
while r:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False

pygame.quit()