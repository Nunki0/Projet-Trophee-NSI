import pygame
import player
import point


def Start():
    """initialisation de la fenêtre"""
    global screen, player, pt, locations
    screen = pygame.display.set_mode((1400,690))
    pygame.display.set_caption("Explore")
    background = pygame.image.load("Carte.jpg")
    screen.blit(background, (0,0))
    player = player.Explorer(0,0)
    pt = point.Point(150,200)
    locations = {
        "Europe": {
                "France":["Paris",402,150]
        },
        "Asie": {
                "Japon":["Tokyo",960,180]
        },
        "Afrique": {
                "Tchad":["N'Djamena",650,700]
        }
    }
    mark_country("France")

def sprite_display():
    """gestion de l'image des sprites"""
    screen.blit(player.get_image(), player.get_position())
    screen.blit(pt.get_image(), pt.get_position())
      
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


def mark_country(country):
    """affiche un point sur le pays indiqué"""
    for i in locations:
        for k in locations[i]:
            if country == k:
                npoint = point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
            




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
