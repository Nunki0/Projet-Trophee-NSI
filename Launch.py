import interface
import pygame
from game import *

def global_init():
    pygame.init()
    Start(interface.Réglages()) #initialisation fenêtre #interface.Réglages()

global_init()
run() #boucle de jeu
