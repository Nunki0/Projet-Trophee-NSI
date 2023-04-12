import pygame
import Sprite

class Explorer(Sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("player.png").convert_alpha()
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.speed = 3
        self.animation_images = {
            'down':self.get_image(0,0),
            'left':self.get_image(0,0),
            'right': self.get_image(0,0),
            'up': self.get_image(0,0),
            'basic' :self.get_image(0,0),
              }
        
    def get_image(self, x=0, y=0):
        """renvoie l'image du sprite"""
        image = self.create_image(x,y,180,130,self.sprite_sheet)
        image.set_colorkey([255,255,255])
        return image
    
    def goto(self,x,y):
        self.rect.center = [x,y]

    def move_right(self):
        self.goto(self.rect.centerx+self.speed, self.rect.centery)

    
        


