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
                "Biélorussie":["Minsk",882,287],#fait
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
                "Liechtenstein":["Vaduz",605,406],
                "Lituanie":["Vilnius",830,255],#fait
                "Luxembourg":["Luxembourg",548,354],#fait
                "Macédoine du Nord":["Skopje",798,511],
                "Malte":["La Valette",683,632],
                "Moldavie":["Chişinău",904,405],
                "Monaco":["Monaco",563,474],
                "Monténégro":["Podgorica",759,494],#fait
                "Norvège":["Oslo",618,161],
                "Pays-Bas":["Amsterdam",531,295],#fait
                "Pologne":["Varsovie",795,351],
                "Portugal":["Lisbonne",294,573],
                "Roumanie":["Bucarest",863,450],
                "Royaume-Uni":["Londres",450,318],
                "Russie":["Moscou",1005,215],
                "Saint-Marin":["Saint-Marin",648,473],#fait
                "Serbie":["Belgrade",776,448],
                "Slovaquie":["Bratislava",720,383],#fait
                "Slovénie":["Ljubljana",680,427],
                "Suède":["Stockholm",718,173],#fait
                "Suisse":["Berne",565,408],#fait
                "Tchéquie":["Prague",678,350],#fait
                "Ukraine":["Kiev",926,336]#fait
        },
        "Asie": {
                "Afghanistan":["Kaboul",0,0],
                "Arabie saoudite":["Riyad",0,0],
                "Arménie":["Erevan",0,0],
                "Azerbaïdjan":["Bakou",0,0],
                "Bahreïn":["Manama",0,0],
                "Bangladesh":["Dacca",0,0],
                "Bhoutan":["Timphou",0,0],
                "Birmanie":["Naypyidaw",0,0],
                "Brunei":["Bandar Seri Begawan",0,0],
                "Cambodge":["Phnom Penh",0,0],
                "Chine":["Pékin",0,0],
                "Corée du Nord":["Pyongyang",0,0],
                "Corée du Sud":["Séoul",0,0],
                "Émirats arabes unis":["Abu Dabi",0,0],
                "Géorgie":["Tbilissi",0,0],
                "Inde":["New Dehli",0,0],
                "Indonésie":["Jakarta",0,0],
                "Irak":["Bagdad",0,0],
                "Iran":["Téhéran",0,0],
                "Israël":["Jérusalem",0,0],
                "Japon":["Tokyo",1200,240],
                "Jordanie":["Amman",0,0],
                "Kazakhstan":["Astana"],
                "Kirghizistan":["Bichkek"],
                "Koweït":["Koweït",0,0],
                "Laos":["Vietnane",0,0],
                "Liban":["Beyrouth",0,0],
                "Malaisie":["Kuala Lumpur",0,0],
                "Maldives":["Malé",0,0],
                "Mongolie":["Oulan-Bator",0,0],
                "Népal":["Katmandou",0,0],
                "Oman":["Mascate",0,0],
                "Ouzbékistan":["Tachkent",0,0],
                "Pakistan":["Islamabad"],
                "Philippines":["Manille"],
                "Qatar":["Doha",0,0],
                "Russie":["Moscou",0,0],
                "Singapour":["Singapour",0,0],
                "Sri Lanka":["Sri Jayawardenapura Kotte",0,0],
                "Syrie":["Damas",0,0],
                "Tadjikistan":["Douchanbé",0,0],
                "Taïwan":["Taipei",0,0],
                "Thaïlande":["Bangkok",0,0],
                "Timor oriental":["Dili",0,0],
                "Turkménistan":["Achgabat",0,0],
                "Turquie":["Ankara",0,0],
                "Viêt Nam":["Hanoï",0,0],
                "Yémen":["Sanaa",0,0]
        },
        "Afrique": {
                "Afrique du Sud":["Pretoria",0,0],
                "Algérie":["Alger",0,0],
                "Angola":["Luanda",0,0],
                "Bénin":["Porto-Novo",0,0],
                "Botswana":["Gaborone",0,0],
                "Burkina Faso":["Ouagadougou",0,0],
                "Burundi":["Gitega",0,0],
                "Cameroun":["Yaoundé",0,0],
                "Cap-Vert":["Praia",0,0],
                "République Centrafricaine":["Bangui",0,0],
                "Comores":["Moroni",0,0],
                "République du Congo":["Brazzaville"],
                "République Démocratique du Congo":["Kinshasa",0,0],
                "Côte d'Ivoire":["Yamoussoukro",0,0],
                "Djibouti":["Djibouti",0,0],
                "Égypte":["Le Caire",0,0],
                "Érythrée":["Asmara",0,0], 
                "Eswatini":["M'Babane",0,0],
                "Éthiopie":["Addis Abeba",0,0],
                "Gabon":["Libreville",0,0], 
                "Gambie":["Banjul",0,0],
                "Ghana":["Accra",0,0], 
                "Guinée":["Conakry",0,0],
                "Guinée-Bissau":["Bissau",0,0], 
                "Guinée Equatoriale":["Malabo",0,0], 
                "Kenya":["Nairobi",0,0], 
                "Lesotho":["Maseru",0,0], 
                "Liberia":["Monrovia",0,0], 
                "Libye":["Tunis",0,0], 
                "Madagascar":["Tanarive",0,0],
                "Malawi":["Lilongwe",0,0],
                "Mali":["Bamako",0,0], 
                "Maroc":["Rabat",0,0],
                "Maurice":["Port-Louis",0,0], 
                "Mauritanie":["Nouakchott",0,0], 
                "Mozambique":["Maputo",0,0], 
                "Namibie":["Windhoek",0,0], 
                "Niger":["Niamey",0,0], 
                "Nigeria":["Abuja",0,0], 
                "Ouganda":["Kampala",0,0], 
                "Rwanda":["Kigali",0,0], 
                "São Tomé-et-Principe":["São Tomé",0,0],
                "Sénégal":["Dakar",0,0],
                "Seychelles":["Victoria",0,0], 
                "Sierra Leone":["Freetown",0,0], 
                "Somalie":["Mogadisco",0,0], 
                "Soudan":["Khartoum",0,0], 
                "Soudan du Sud":["Djouba",0,0],
                "Tanzanie":["Dodoma",0,0],
                "Tchad":["N'Djamena",750,340],
                "Togo":["Lomé",0,0], 
                "Tunisie":["Tunis",0,0], 
                "Zambie":["Lusaka",0,0], 
                "Zimbabwe":["Harare",0,0]        
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
