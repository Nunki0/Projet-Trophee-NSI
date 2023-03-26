import pygame
import Sprite

class point(Sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        sprite_sheet = pygame.image.load("Point_noir.png").convert_alpha()
        image = self.image(0,0,900,724,sprite_sheet)
        rect = image.get_rect()
        self.position =[x,y]