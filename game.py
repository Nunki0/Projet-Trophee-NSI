import pygame
import player
import Point


def Start(zone):
    """initialisation de la fenêtre"""
    global sprites, locations, player
    load_map(zone)
    sprites = pygame.sprite.Group()
    player = player.Explorer(0,0)
    sprites.add(player)
    locations = {
        "Europe": {
                "Albanie":["Tirana",772,524], #fait
                "Allemagne":["Berlin",670,313],#fait
                "Autriche":["Vienne",708,384],#fait
                "Belgique":["Bruxelles",530,334],#fait
                "Biélorussie":["Minsk",870,270],#fait
                "Bosnie-Herzégovine":["Sarajevo",736,464],#fait
                "Bulgarie":["Sofia",820,492],#fait
                "Chypre":["Nicosie",1004,646],#fait
                "Croatie":["Zagreb",714,430],#fait
                "Danemark":["Copenhague",636,245],#fait
                "Espagne":["Madrid",387,539],#fait
                "Estonie":["Tallinn",818,170],#fait
                "Finlande":["Helsinki",825,147],#fait
                "France":["Paris",487,378],#fait
                "Grèce":["Athènes",834,584],#fait
                "Hongrie":["Budapest",758,401],#fait
                "Irlande":["Dublin",350,290],#fait
                "Islande":["Reykjavik",179,81],#fait
                "Italie":["Rome",662,515],#fait
                "Kosovo":["Pristina",784,495],#fait
                "Lettonie":["Riga",812,215],#fait
                "Liechtenstein":["Vaduz",709,416],
                "Lituanie":["Vilnius",830,255],#fait
                "Luxembourg":["Luxembourg",548,354],#fait
                "Macédoine du Nord":["Skopje",780,500],
                "Malte":["La Valette",0,0],
                "Moldavie":["Chişinău",0,0],
                "Monaco":["Monaco",0,0],
                "Monténégro":["Podgorica",759,494],#fait
                "Norvège":["Oslo",0,0],
                "Pays-Bas":["Amsterdam",531,295],#fait
                "Pologne":["Varsovie",795,351],
                "Portugal":["Lisbonne",0,0],
                "Roumanie":["Bucarest",0,0],
                "Royaume-Uni":["Londres",0,0],
                "Russie":["Moscou",0,0],
                "Saint-Marin":["Saint-Marin",648,473],#fait
                "Serbie":["Belgrade",0,0],
                "Slovaquie":["Bratislava",720,383],#fait
                "Slovénie":["Ljubljana",0,0],
                "Suède":["Stockholm",718,173],#fait
                "Suisse":["Berne",565,408],#fait
                "Tchéquie":["Prague",678,350],#fait
                "Ukraine":["Kiev",926,336]#fait
        },
        "Asie": {
                "Japon":["Tokyo",1200,240]
        },
        "Afrique": {
                "Tchad":["N'Djamena",750,340]
        }
    }
    mark_zone(zone)

def load_map(zone):
    global screen
    screen_x = 1360
    screen_y = 690
    zones = {
        "Europe":[1.3,1500,210], #Carte.jpg: [3.4,540,60]
        "Asie":[0.8,2400,200],
        "Afrique":[0.6,850,650]
    }
    zoom = zones[zone][0]
    surf_x = round(screen_x/zoom)
    surf_y = round(screen_y/zoom)
    screen = pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption("Explore")
    background = pygame.image.load("Carte1.png")
    surf = pygame.Surface([surf_x,surf_y])
    surf.blit(background,(0,0),(zones[zone][1],zones[zone][2],surf_x,surf_y))
    surf2=pygame.transform.scale_by(surf,zoom)
    screen.blit(surf2, (0,0))

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
                npoint = Point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
                sprites.add(npoint)

def mark_all():
    """affiche tous les pays"""
    for i in locations:
        for k in locations[i]:
            npoint = Point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
            sprites.add(npoint)

def mark_zone(zone):
    """affiche tous les pays d'une zone géographique"""
    for i in locations:
        if i == zone:
            for k in locations[i]:
                npoint = Point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
                sprites.add(npoint)
                
def run():
    """boucle du jeu"""
    clock =pygame.time.Clock()
    running =True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN: # lorsque l'on clique
                print(pygame.mouse.get_pos())        # affiche les coordonnées du pointeur de souris pour avoir plus facilement les coordonnées des capitales à entrer dans le dict
        inputs()
        sprites.draw(screen)
        pygame.display.flip()

        clock.tick(50)
    pygame.quit()
