import pygame



def __init__():
    sprite_sheet = pygame.image.load('Flèche.png').convert_alpha()
    image = pygame.Surface([97,97])
    image.blit(sprite_sheet,(0,0), (0,0,97,97))
    image.set_colorkey([255,255,255])
    rect = image.get_rect()
    position =[0,0]
        