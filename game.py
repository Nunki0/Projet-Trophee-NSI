import pygame


def __init__():
        # fenetre du jeux
        screen = pygame.display.set_mode((1000,650))
        pygame.display.set_caption("Explore")


def run():
        #boucle de jeux
        clock =pygame.time.Clock()
        running =True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(50)
        pygame.quit()
