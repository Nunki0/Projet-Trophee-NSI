import pygame
import sprite

class Explorer(sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Flèche.png").convert_alpha()
        self.position =[x,y]
        self.rect = self.get_image().get_rect()
        self.speed = 3

    def get_image(self):
        image = self.image(0,0,225,225,self.sprite_sheet)
        image.set_colorkey([255,255,255])
        return image
    

        


