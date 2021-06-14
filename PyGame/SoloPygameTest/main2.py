import pygame
import os 
from conf import ASSETS_DIR, walkRight, walkLeft
pygame.init()

WIN = pygame.display.set_mode((500,480))
pygame.image.load(os.path.join(ASSETS_DIR, 'L1.png')),
pygame.display.set_caption("First Game")

x = 50
y = 400
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
bg_h , bg_w = 500, 589 # this is needed as width, height is for the char __should be renamed really__


    
BG = pygame.transform.scale(pygame.image.load(
    os.path.join(ASSETS_DIR, 'bg.jpg')), (bg_h, bg_w))
    
char = pygame.image.load(os.path.join(ASSETS_DIR, 'standing.png'))

clock = pygame.time.Clock()




def redrawGameWindow():
    global walkCount
    WIN.blit(BG, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        WIN.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        WIN.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        WIN.blit(char, (x,y))
    
    pygame.display.update()


#mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_d] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
            
    redrawGameWindow()

pygame.quit()