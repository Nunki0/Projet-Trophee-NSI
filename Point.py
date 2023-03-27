import pygame
import sprite

class point(sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Point_noir.png").convert_alpha()
        self.position =[x,y]
        self.rect = self.get_image().get_rect()

    def get_image(self):
        image = self.create_image(0,0,80,64,self.sprite_sheet)
        image.set_colorkey([255,255,255])
        return image
    def get_position(self):
        return tuple(self.position)