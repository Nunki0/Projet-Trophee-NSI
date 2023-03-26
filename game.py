import pygame
import Player
import Point


def Start():
    # fenetre du jeux
    global screen
    screen = pygame.display.set_mode((1400,690))
    pygame.display.set_caption("Explore")
    background = pygame.image.load("Carte.jpg")
    screen.blit(background, (0,0))
    global player
    player = Player.explorer(0,0)
    global sprites
    sprites = pygame.sprite.Group()
    sprites.add(player)

def sprite_display(sprite):
    return sprite.get_image()
      
def run():
    #boucle de jeux
    clock =pygame.time.Clock()
    running =True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(50)
        screen.blit(sprite_display(player), (0,0))
        pygame.display.update()
    pygame.quit()
