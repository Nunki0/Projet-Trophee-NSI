
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png').convert_alpha()
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
        self.speed = 3
        self.feet = pygame.Rect(0,0,self.rect.width*0.5,12)

    def change_animation(self, name):
        self.current_animation = name

    def move_right(self, walls):
        self.update_position(walls, self.speed)
        self.current_animation = 'right'
        self.image.set_colorkey([0,0,0])

    def move_left(self, walls):
        self.update_position(walls, -self.speed)
        self.current_animation = 'left'
        self.image.set_colorkey([0,0,0])

    def move_up(self, walls):
        self.update_position(walls, 0,-self.speed)
        self.current_animation = 'up'
        self.image.set_colorkey([0,0,0])

    def move_down(self, walls):
        self.update_position(walls, 0,self.speed)
        self.current_animation = 'down'
        self.image.set_colorkey([0,0,0])

    def update_position(self, walls, x=0, y=0):
        new_rect = pygame.Rect(self.feet[0]+x, self.feet[1]+y, self.feet[2], self.feet[3])
        if new_rect.collidelist(walls)==-1:
            self.position[0] += x
            self.position[1] += y

    def update(self):
        self.rect.topleft = self.position
        self.image = self.animation_images[self.current_animation]


    def get_image(self,x,y):
        image = pygame.Surface([97,97])
        image.blit(self.sprite_sheet, (0,0), (x,y,97,97))
        return image
