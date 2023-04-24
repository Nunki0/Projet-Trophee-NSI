import pygame
import player
import Point


def Start(zone):
    """initialisation de la fenêtre"""
    global sprites, locations, player, couleurs
    load_map(zone)
    sprites = pygame.sprite.Group()
    player = player.Explorer(0,0)
    sprites.add(player)
    couleurs = {
        "noir":(0,0,0),
        "vert":(0,255,255),
        "rouge":(255,255,0)
    }
    locations = {
        "Europe": {
                "Albanie":["Tirana",772,524], 
                "Allemagne":["Berlin",670,313],
                "Autriche":["Vienne",708,384],
                "Belgique":["Bruxelles",530,334],
                "Biélorussie":["Minsk",882,287],
                "Bosnie-Herzégovine":["Sarajevo",736,464],
                "Bulgarie":["Sofia",820,492],
                "Chypre":["Nicosie",1004,646],
                "Croatie":["Zagreb",714,430],
                "Danemark":["Copenhague",636,245],
                "Espagne":["Madrid",387,539],
                "Estonie":["Tallinn",818,170],
                "Finlande":["Helsinki",825,147],
                "France":["Paris",487,378],
                "Grèce":["Athènes",834,584],
                "Hongrie":["Budapest",758,401],
                "Irlande":["Dublin",350,290],
                "Islande":["Reykjavik",179,81],
                "Italie":["Rome",662,515],
                "Kosovo":["Pristina",784,495],
                "Lettonie":["Riga",812,215],
                "Liechtenstein":["Vaduz",605,406],
                "Lituanie":["Vilnius",830,255],
                "Luxembourg":["Luxembourg",548,354],
                "Macédoine du Nord":["Skopje",798,511],
                "Malte":["La Valette",683,632],
                "Moldavie":["Chişinău",904,405],
                "Monaco":["Monaco",563,474],
                "Monténégro":["Podgorica",759,494],
                "Norvège":["Oslo",618,161],
                "Pays-Bas":["Amsterdam",531,295],
                "Pologne":["Varsovie",795,351],
                "Portugal":["Lisbonne",294,573],
                "Roumanie":["Bucarest",863,450],
                "Royaume-Uni":["Londres",450,318],
                "Russie":["Moscou",1005,215],
                "Saint-Marin":["Saint-Marin",648,473],
                "Serbie":["Belgrade",776,448],
                "Slovaquie":["Bratislava",720,383],
                "Slovénie":["Ljubljana",680,427],
                "Suède":["Stockholm",718,173],
                "Suisse":["Berne",565,408],
                "Tchéquie":["Prague",678,350],
                "Ukraine":["Kiev",926,336]
        },
        "Asie": {
                "Afghanistan":["Kaboul",440,190],
                "Arabie saoudite":["Riyad",237,300],
                "Arménie":["Erevan",215,137],
                "Azerbaïdjan":["Bakou",259,138],
                "Bahreïn":["Manama",282,290],
                "Bangladesh":["Dacca",658,315],
                "Bhoutan":["Timphou",650,279],
                "Myanmar":["Naypyidaw",724,350],
                "Brunei":["Bandar Seri Begawan",914,528],
                "Cambodge":["Phnom Penh",812,447],
                "Chine":["Pékin",850,145],
                "Corée du Nord":["Pyongyang",938,153],
                "Corée du Sud":["Séoul",961,168],
                "Émirats arabes unis":["Abu Dabi",329,312],
                "Géorgie":["Tbilissi",203,120],
                "Inde":["New Dehli",524,270],
                "Indonésie":["Jakarta",0,0],
                "Irak":["Bagdad",0,0],
                "Iran":["Téhéran",0,0],
                "Israël":["Jérusalem",0,0],
                "Japon":["Tokyo",1076,192],
                "Jordanie":["Amman",152,234],
                "Kazakhstan":["Astana",404,25],
                "Kirghizistan":["Bichkek",479,116],
                "Koweït":["Koweït",255,256],
                "Laos":["Vietnane",787,377],
                "Liban":["Beyrouth",142,206],
                "Malaisie":["Kuala Lumpur",790,544],
                "Maldives":["Malé",508,513],
                "Mongolie":["Oulan-Bator",724,46],
                "Népal":["Katmandou",599,271],
                "Oman":["Mascate",366,326],
                "Ouzbékistan":["Tachkent",436,129],
                "Pakistan":["Islamabad",478,202],
                "Philippines":["Manille",967,420],
                "Qatar":["Doha",294,302],
                "Singapour":["Singapour",815,564],
                "Sri Lanka":["Sri Jayawardenapura Kotte",581,501],
                "Syrie":["Damas",154,204],
                "Tadjikistan":["Douchanbé",439,157],
                "Taïwan":["Taipei",951,305],
                "Thaïlande":["Bangkok",770,426],
                "Timor oriental":["Dili",1023,672],
                "Turkménistan":["Achgabat",329,155],
                "Turquie":["Ankara",110,141],
                "Viêt Nam":["Hanoï",810,343],
                "Yémen":["Sanaa",238,410]
        },
        "Afrique": {
                "Afrique du Sud":["Pretoria",824,601],
                "Algérie":["Alger",615,23],
                "Angola":["Luanda",700,446],
                "Bénin":["Porto-Novo",609,301],
                "Botswana":["Gaborone",797,587],
                "Burkina Faso":["Ouagadougou",574,246],
                "Burundi":["Gitega",834,398],
                "Cameroun":["Yaoundé",689,321],
                "Cap-Vert":["Praia",397,220],
                "République Centrafricaine":["Bangui",742,312],
                "Comores":["Moroni",950,475],
                "République du Congo":["Brazzaville",712,395],
                "République Démocratique du Congo":["Kinshasa",714,414],
                "Côte d'Ivoire":["Yamoussoukro",545,299],
                "Djibouti":["Djibouti",938,253],
                "Égypte":["Le Caire",833,88],
                "Érythrée":["Asmara",904,217], 
                "Eswatini":["M'Babane",844,608],
                "Éthiopie":["Addis Abeba",906,278],
                "Gabon":["Libreville",670,362], 
                "Gambie":["Banjul",458,237],
                "Ghana":["Accra",588,307], 
                "Guinée":["Conakry",475,264],
                "Guinée-Bissau":["Bissau",465,251], 
                "Guinée Equatoriale":["Malabo",661,333], 
                "Kenya":["Nairobi",897,370], 
                "Lesotho":["Maseru",816,639], 
                "Liberia":["Monrovia",505,303], 
                "Libye":["Tripoli",701,59], 
                "Madagascar":["Tanarive",978,524],
                "Malawi":["Lilongwe",870,492],
                "Mali":["Bamako",532,243], 
                "Maroc":["Rabat",538,50],
                "Maurice":["Port-Louis",1056,553], 
                "Mauritanie":["Nouakchott",463,187], 
                "Mozambique":["Maputo",854,602], 
                "Namibie":["Windhoek",731,564], 
                "Niger":["Niamey",614,233], 
                "Nigeria":["Abuja",650,276], 
                "Ouganda":["Kampala",857,350], 
                "Rwanda":["Kigali",836,379], 
                "São Tomé-et-Principe":["São Tomé",643,362],
                "Sénégal":["Dakar",452,223],
                "Seychelles":["Victoria",1046,407], 
                "Sierra Leone":["Freetown",482,284], 
                "Somalie":["Mogadisco",950,350], 
                "Soudan":["Khartoum",865,211], 
                "Soudan du Sud":["Djouba",849,313],
                "Tanzanie":["Dodoma",881,422],
                "Tchad":["N'Djamena",714,251],
                "Togo":["Lomé",599,302], 
                "Tunisie":["Tunis",676,19], 
                "Zambie":["Lusaka",822,494], 
                "Zimbabwe":["Harare",840,535]        
        }
    }
    mark_zone(zone)

def load_map(zone):
    """charge la carte de jeu, ajustée sur la zone choisie"""
    global screen
    screen_x = 1360
    screen_y = 690
    zones = {
        "Europe":[1.3,1500,210], 
        "Asie":[0.7,2100,430],
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

def mark_zone(zone):
    """affiche tous les pays d'une zone géographique"""
    for i in locations:
        if i == zone:
            for k in locations[i]:
                npoint = Point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
                sprites.add(npoint)

def text_display():
    font1 = pygame.font.SysFont(None, 72)
    img1 = font1.render('test', True, couleurs["noir"])
    screen.blit(img1,(150,150))

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
        text_display()
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()
