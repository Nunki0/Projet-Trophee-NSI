import pygame
from game import *

def global_init():
    pygame.init()
    Start("Europe") #initialisation fenêtre

global_init()
run() #boucle de jeu
