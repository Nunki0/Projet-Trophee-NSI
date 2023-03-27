import pygame
import sprite

class Explorer(sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("Flèche.png").convert_alpha()
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.speed = 3

    def get_image(self):
        """renvoie l'image du sprite"""
        image = self.create_image(0,0,225,225,self.sprite_sheet)
        image.set_colorkey([255,255,255])
        return image
    
    def goto(self,x,y):
        self.rect.center = [x,y]

    def move_right(self):
        self.goto(self.rect.centerx+self.speed, self.rect.centery)

    
        


