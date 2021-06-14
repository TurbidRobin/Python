import pygame
import os

from pygame.constants import RESIZABLE 


from conf import ASSETS_DIR, walkRight, walkLeft

ASSETS_DIR = os.path.join(ASSETS_DIR)

WIDTH , HEIGHT = 1000, 700
#BG_W, BG_H = 500, 589 not needed for this (?) ##look at main2.py for the reason for this##

BORDER = pygame.Rect(WIDTH // 2 -5, 0, 10, HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)

BG = pygame.transform.scale(pygame.image.load(
    os.path.join(ASSETS_DIR, 'bg.jpg')), (WIDTH, HEIGHT))

FPS = 60
VEL = 5 


def bg_test():
    WIN.blit(BG, (0,0))


    pygame.display.update()

def player_movment(keys_pressed, player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0: # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_d] and player.x + VEL + player.width < BORDER.x: # RIGHT
        player.x += VEL
    if keys_pressed[pygame.K_w] and player.y - VEL > 0: # UP
        player.y -= VEL
    if keys_pressed[pygame.K_s] and player.y + VEL + player.width < HEIGHT: # DOWN
        player.y += VEL
    
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        bg_test()

    main()

if __name__ == "__main__":
    main()
