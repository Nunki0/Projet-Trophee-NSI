import pygame
import Game
import Player

def global_init():
    pygame.init()
    Game.__init__()
    Player.__init__()

Game.run()
