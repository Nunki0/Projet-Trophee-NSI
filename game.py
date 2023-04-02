import pygame
import player
import point


def Start():
    """initialisation de la fenêtre"""
    screen_x = 1400
    screen_y = 690
    zoom = 1.5
    surf_x = round(screen_x/zoom)
    surf_y = round(screen_y/zoom)
    global screen, sprites, locations, player
    screen = pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption("Explore")
    background = pygame.image.load("Carte.jpg")
    surf = pygame.Surface([surf_x,surf_y])
    surf.blit(background,(0,0))
    surf2=pygame.transform.scale_by(surf,zoom)
    screen.blit(surf2, (0,0))
    sprites = pygame.sprite.Group()
    player = player.Explorer(0,0)
    sprites.add(player)
    locations = {
        "Europe": {
                "France":["Paris",695,185],
                "Albanie":["Tirana",715,210],
                "Allemagne":["Berlin",730,185],
                "Autriche":["Vienne",715,200],
                "Belgique":["Bruxelles",705,175],
                "Biélorussie":["Minsk",740,170],
                "Bosnie-Herzégovine":["Sarajevo",720,210],
                "Bulgarie":["Sofia",730,215],
                "Croatie":["Zagreb",720,200],
                "Danemark":["Copenhague",715,170]
        },
        "Asie": {
                "Japon":["Tokyo",1200,240]
        },
        "Afrique": {
                "Tchad":["N'Djamena",750,340]
        }
    }
    mark_zone("Europe")

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
                sprites.add(npoint)
                print(k, "marked")

def mark_all():
    """affiche tous les pays"""
    for i in locations:
        for k in locations[i]:
            npoint = point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
            sprites.add(npoint)

def mark_zone(zone):
    """affiche tous les pays d'une zone géographique"""
    for i in locations:
        if i == zone:
            for k in locations[i]:
                npoint = point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
                sprites.add(npoint)
                
def run():
    """boucle du jeu"""
    clock =pygame.time.Clock()
    running =True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        inputs()
        sprites.draw(screen)
        pygame.display.update()
        clock.tick(50)
    pygame.quit()
