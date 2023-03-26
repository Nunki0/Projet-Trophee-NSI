import pygame


class explorer(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        sprite_sheet = pygame.image.load('Flèche.png').convert_alpha()
        image = pygame.Surface([225,225])
        image.blit(sprite_sheet,(0,0), (0,0,97,97))
        image.set_colorkey([255,255,255])
        rect = image.get_rect()
        rect.center = [0,0]

        