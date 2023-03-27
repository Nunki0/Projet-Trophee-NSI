import pygame
import player
import point


def Start():
    """initialisation de la fenêtre"""
    global screen
    screen = pygame.display.set_mode((1400,690))
    pygame.display.set_caption("Explore")
    background = pygame.image.load("Carte.jpg")
    screen.blit(background, (0,0))
    global player
    player = player.Explorer(0,0)
    global pt
    pt = point.point(150,50)

def sprite_display():
    """gestion de l'image des sprites"""
    screen.blit(player.get_image(), player.get_position())
    screen.blit(pt.get_image(), (0,0))
      
def inputs():
    """gestion des entrées clavier"""
    pressed = pygame.key.get_pressed()    
    if pressed[pygame.K_LEFT]:
        player.move_left()
    if pressed[pygame.K_RIGHT]:
        player.move_right()
    if pressed[pygame.K_UP]:
        player.move_up()
    if pressed[pygame.K_DOWN]:
        player.move_down()
    
def run():
    """boucle du jeu"""
    clock =pygame.time.Clock()
    running =True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        inputs()
        sprite_display()
        pygame.display.update()
        clock.tick(50)
    pygame.quit()
