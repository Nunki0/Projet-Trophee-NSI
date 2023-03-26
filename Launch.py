import pygame
import Game
import Player

def global_init():
    pygame.init()
    Game.__init__()
    Player.__init__()

global_init()
Game.run()
