
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('Projet-Trophee-NSI\player.png').convert_alpha()
        self.image = self.get_image(0,0)
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.position =[x,y]
        self.animation_images = {
            'down':self.get_image(0,300),
            'left':self.get_image(0,200),
            'right': self.get_image(0,100),
            'up': self.get_image(0,400),
            'basic' :self.get_image(0,0),
        }
        self.current_animation = 'left'
        self.speed=2

    def change_animation(self, name):
        self.current_animation = name

    def move_right(self):
        self.position[0] +=self.speed
        self.current_animation = 'right'
        self.image.set_colorkey([0,0,0])

    def move_left(self):
        self.position[0] -=self.speed
        self.current_animation = 'left'
        self.image.set_colorkey([0,0,0])

    def move_up(self):
        self.position[1] -=self.speed
        self.current_animation = 'up'
        self.image.set_colorkey([0,0,0])

    def move_down(self):
        self.position[1] +=self.speed
        self.current_animation = 'down'
        self.image.set_colorkey([0,0,0])

    def update(self):
        self.rect.topleft = self.position
        self.image = self.animation_images[self.current_animation]


    def get_image(self,x,y):
        image = pygame.Surface([97,97])
        image.blit(self.sprite_sheet, (0,0), (x,y,97,97))
        return image
