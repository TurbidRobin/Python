import pygame



def get_sprite(self, x , y, w, h):
    sprite = pygame.Surface((w,h))
    sprite.set_colorkey((128,128,128))
    sprite.blit(self.sprite_sheet(0,0),(x,y,w,h))
    return sprite