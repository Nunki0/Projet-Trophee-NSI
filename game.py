import pygame


def __init__():
        # fenetre du jeux
        screen = pygame.display.set_mode((1400,690))
        pygame.display.set_caption("Explore")
        background = pygame.image.load("Carte.jpg")
        screen.blit(background, (0,0))


def run():
        #boucle de jeux
        clock =pygame.time.Clock()
        running =True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(50)
            pygame.display.update()
        pygame.quit()
