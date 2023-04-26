import pygame
import sprite

class Point(sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Point_noir.png").convert_alpha()
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def get_image(self):
        image = self.create_image(0,0,25,20,self.sprite_sheet)
        image.set_colorkey([255,255,255])
        return image

    def return_rect(self):
        return self.rect