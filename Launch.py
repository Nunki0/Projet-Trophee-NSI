import pygame
from game import *

def global_init():
    pygame.init()
    Start() #initialisation fenêtre

global_init()
run() #boucle de jeu
