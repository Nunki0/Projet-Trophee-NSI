import pygame
import Game
import Player

def global_init():
    pygame.init()
    Game.__init__()
    Player.explorer(0,0)

global_init()
Game.run()
