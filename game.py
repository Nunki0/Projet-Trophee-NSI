
import pygame

import pytmx
import pyscroll
from player import Player


class Game:

    def __init__(self):

        # fenetre du jeux
        self.screen =pygame.display.set_mode((800,600))
        pygame.display.set_caption("Pygamon")

        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame("Map2.tmx")
        map_data = pyscroll.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur
        Player_position = tmx_data.get_object_by_name("player")
        self.player = Player(Player_position.x, Player_position.y)

        # definir une liste pour les collision
        self.walls =[]

        for obj in tmx_data.objects:
             if obj.name =="collision":
                  self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calque 
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=7)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
        elif pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')



        

    def run(self):
        #boucle de jeux
        clock =pygame.time.Clock()
        running =True

        while running:

            # Gérer les entrées du joueur
            self.handle_input()

            self.group.center(self.player.rect)

            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running =False

            clock.tick(60)

        pygame.quit()
