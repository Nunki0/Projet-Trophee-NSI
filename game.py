import pygame
import Player
import Point


def Start():
    # fenetre du jeux
    global screen
    screen = pygame.display.set_mode((1400,690))
    pygame.display.set_caption("Explore")
    background = pygame.image.load("Carte.jpg")
    screen.blit(background, (0,0))
    global player
    player = Player.explorer(0,0)
    global pt
    pt = Point.point(150,50)

def sprite_display(sprite):
    return sprite.get_image()
      
def inputs():
    pressed = pygame.key.get_pressed()    
    if pressed[pygame.K_LEFT]:
        player.move_left()
    if pressed[pygame.K_RIGHT]:
        player.move_right()
    if pressed[pygame.K_UP]:
        player.move_up()
    if pressed[pygame.K_DOWN]:
        player.move_down()
    
def run():
    #boucle de jeux
    clock =pygame.time.Clock()
    running =True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        inputs()
        screen.blit(sprite_display(player), (0,0))
        screen.blit(sprite_display(pt), (0,0))
        pygame.display.update()
        clock.tick(50)
    pygame.quit()
