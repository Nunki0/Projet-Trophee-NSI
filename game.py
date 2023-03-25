import pygame

def run(self):
        #boucle de jeux
        clock =pygame.time.Clock()
        running =True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running =False
            clock.tick(50)
        pygame.quit()
