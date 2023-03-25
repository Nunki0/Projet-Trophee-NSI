import pygame

def __init__():
    sprite_sheet = pygame.image.load('player.png').convert_alpha()
    image = sprite_sheet.get_image(0,0)