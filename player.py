import pygame
import sprite
import time

class Explorer(sprite.Sprites):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_sheet = pygame.image.load("player.png").convert_alpha()
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.speed = 4
        self.animation_images = {
            'down':self.get_image(0,0),
            'right':self.get_image(0,68),
            'left':self.get_image(0,137),
            'up': self.get_image(0,420),
            }

    def get_image(self, x=0, y=0):
        """renvoie l'image du sprite"""
        image = self.create_image(x,y,91,71,self.sprite_sheet)
        image.set_colorkey([255,255,255])
        return image
    
    def goto(self,x,y):
        self.rect.center = [x,y]

    def move_right(self):
        self.goto(self.rect.centerx+self.speed, self.rect.centery)
        self.image=self.animation_images["right"]
        
    def move_left(self):
        self.goto(self.rect.centerx-self.speed, self.rect.centery)
        self.image = self.animation_images["left"]

    def move_up(self):
        self.goto(self.rect.centerx, self.rect.centery-self.speed)
        self.image = self.animation_images['up']
    
    def move_down(self):
        self.goto(self.rect.centerx, self.rect.centery+self.speed)
        self.image = self.animation_images['down']

    def colision(self, rect):
        return self.rect.collidelistall(rect) #renvoie la liste des indices rectangles intersectant le rectangle du joueur
    
        


