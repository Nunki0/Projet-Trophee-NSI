import pygame
import player
import point
import random

def Start(réglages):
    """initialisation de la fenêtre"""
    global sprites, locations, player, couleurs, zone, values, elements, current_element, point_list, point_rect_list
    mode = réglages[1]
    zone = réglages[0]
    load_map(zone)
    sprites = pygame.sprite.Group() #groupe contenant tous les points ainsi que le joueur pour faciliter l'affichage
    player = player.Explorer(500,500)
    point_list = []  #liste des instances de la classe point, utilisée pour cible le point à mettre en vert
    point_rect_list = [] #liste des rectangles correspondants à tous les points pour tester les collisions avec le rectangle du joueur
    couleurs = { #dict des couleurs prédéfinies pour l'affichage de texte à l'écran
        "noir":(0,0,0),
        "vert":(0,255,0),
        "rouge":(255,0,0)
    }

    locations = {
        "Europe": {
                "Albanie":["Tirana",772,524], 
                "Allemagne":["Berlin",670,313],
                "Andorre":["Andorre-la-Vieille",473,498],
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
                "Indonésie":["Jakarta",833,647],
                "Irak":["Bagdad",220,212],
                "Iran":["Téhéran",280,188],
                "Israël":["Jérusalem",137,228],
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
    sprites.add(player) #à laisser après mark_zone pour avoir le bon ordre des calques
    if mode == "Pays":
        values = list(locations[zone].keys())
    else:
        values = [locations[zone][i][0] for i in locations[zone]] #récupère toutes les capitales (1er élément de chacune des liste)
    elements = values[:]
    random.shuffle(elements)
    current_element = 0

def load_map(zone):
    """charge la carte de jeu, ajustée sur la zone choisie"""
    global screen, surf2
    screen_x = 1360
    screen_y = 690
    réglages_zones = { #dict contenant les régages pour chaque zone de jeu: le zoom nécessaire et la position dans la carte
        "Europe":[1.3,1500,210], 
        "Asie":[0.7,2100,430],
        "Afrique":[0.6,850,650]
    }
    zoom = réglages_zones[zone][0]
    surf_x = round(screen_x/zoom)
    surf_y = round(screen_y/zoom)
    screen = pygame.display.set_mode((screen_x,screen_y))
    pygame.display.set_caption("Explore")
    background = pygame.image.load("Carte1.png")
    surf = pygame.Surface([surf_x,surf_y]) #crée une petite surface 
    surf.blit(background,(0,0),(réglages_zones[zone][1],réglages_zones[zone][2],surf_x,surf_y)) #imprime sur cette surface la zone de la carte spécifiée dans le dict selon le choix de zone de l'utilisateur
    surf2=pygame.transform.scale_by(surf,zoom) #crée une nouvelle surface en grossisant la première à la taille de l'écran
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
                npoint = point.Point(locations[i][k][1],locations[i][k][2]) #crée un nouveau point aux coordonnées du pays, s'il existe dans la liste
                point_list.append(npoint)
                point_rect_list.append(npoint.return_rect())
                sprites.add(npoint)
    
def text_display(text, dest, color="noir", pos = (0,0), size = 72, center = False):
    """affiche le texte en paramètre avec les réglages suivants: surface sur laquelle écrire, position, taille de police, centrage au millieu de la surface"""
    font1 = pygame.font.SysFont(None, size)
    img1 = font1.render(text, True, couleurs[color])
    if center:
        dest.blit(img1, (pos[0]-img1.get_rect().width/2, pos[1]-img1.get_rect().height/2))
    else:
        dest.blit(img1,pos)

def endscreen():
    """affiche la fenêtre de fin"""
    endsurf = pygame.Surface([500,300]) #création d'une nouvelle surface
    endsurf.fill((220,220,220))         #grise
    text_display("Bravo!", endsurf, "vert", (250,150), 75, True) #impression du texte
    screen.blit(endsurf, (1360/2-250,690/2-150)) #centrage de la surface par rapport à l'écran
    pygame.display.flip()
    quit = 0
    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #test pour fermer la fenêtre de jeu
                quit = 1

def run():
    """boucle du jeu"""
    global current_element
    clock =pygame.time.Clock()
    running =True 

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #test pour fermer la fenêtre de jeu
                running = False
        inputs()

        if values.index(elements[current_element]) in player.colision(point_rect_list): #si la liste des indices rects touchés contient l'indice du pays à trouver, 
            point_list[values.index(elements[current_element])].green() #affiche le point touché en vert
            if current_element < len(locations[zone]): #si ce n'est pas le dernier pays
                current_element += 1 #on passe au pays suivant

            if current_element >= len(locations[zone]): #si le dernier pays a été trouvé
                endscreen() #affichage de l'écran de fin
                running = False

        screen.blit(surf2,(0,0)) #réinitialisation de l'écran
        text_display(elements[current_element], screen) #affichage du pays à trouver
        sprites.draw(screen) #affichage des sprites
        pygame.display.flip() #mise à jour de l'écran
        clock.tick(50)
    pygame.quit()
