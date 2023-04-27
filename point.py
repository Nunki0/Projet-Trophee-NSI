import pygame
import sprite

class Point(sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("point.png").convert_alpha()
        self.images = {
            "black":self.get_image(0,0),
            "green":self.get_image(0,20)
        }
        self.image = self.images["black"]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def get_image(self,x,y):
        image = self.create_image(x,y,25,20,self.sprite_sheet)
        image.set_colorkey([255,255,255])
        return image

    def return_rect(self):
        return self.rect
    
    def green(self):
        self.image = self.images["green"]
