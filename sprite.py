import pygame

class Sprites(pygame.sprite.Sprite):
    def create_image(self,x,y,size_x,size_y,image):
        """imprime l'image du sprite sur la surface entrée en paramètre"""
        n_image = pygame.Surface([size_x,size_y]) #création de la surface
        n_image.blit(image,(0,0), (x,y,size_x,size_y)) #impression de l'image
        return n_image
    
