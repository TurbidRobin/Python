import os
import pygame

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
ASSETS_DIR = os.path.join(BASE_DIR, "Assets")

################################################# SIDE SCROLLING MOVMENT ############################################
walkRight = [
    pygame.image.load(os.path.join(ASSETS_DIR, 'R1.png')),
    pygame.image.load(os.path.join(ASSETS_DIR, 'R2.png')),
    pygame.image.load(os.path.join(ASSETS_DIR, 'R3.png')),
    pygame.image.load(os.path.join(ASSETS_DIR, 'R4.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'R5.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'R6.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'R7.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'R8.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'R9.png'))]

walkLeft = [
    pygame.image.load(os.path.join(ASSETS_DIR, 'L1.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'L2.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'L3.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'L4.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'L5.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'L6.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'L7.png')), 
    pygame.image.load(os.path.join(ASSETS_DIR, 'L8.png')),
    pygame.image.load(os.path.join(ASSETS_DIR, 'L9.png')),]