import pygame
class Sprites(pygame.sprite.Sprite):
    def image(self,x,y,size_x,size_y,image):
        n_image = pygame.Surface([size_x,size_y])
        n_image.blit(image,(0,0), (x,y,size_x,size_y))
        return n_image
    
    def goto(self,x,y):
        self.position = [x,y]