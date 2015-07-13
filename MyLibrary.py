
import pygame, sys, time
from pygame.locals import *
from pygame.sprite import *

pygame.init()

# Κλάση Game
class Game():
    col_side = 0
    score = 0

    def __init__(self):
        pass
        
    def printscore(self, surf):
        if Game.col_side == 1:
            Game.score += 1
        elif Game.col_side == 4:
            Game.score -= 5

        Game.col_side= 0 
        my_font = pygame.font.SysFont(None, 64)    
        my_text = my_font.render\
                  (str(Game.score), True, (0,0,0), (155,255,255))  
        surf.blit(my_text, (720, 20))
        

# Υποκλάση Lamp
class Lamp(Sprite):
    def __init__(self, id, createX, createY, dimX, dimY, color, high_color, is_high=False):
        Sprite.__init__(self)
        self.id = id
        self.rect=pygame.Rect(createX, createY, dimX, dimY)     # ορθογώνιο rect της κλάσης Ball  
        self.simple_color=pygame.image.load(color)                # εικόνα image της κλάσης Ball
        self.high_color=pygame.image.load(high_color)
        self.is_high = is_high

    def draw(self, surf):
        if self.is_high :
            surf.blit(self.high_color, self.rect)
        else:
            surf.blit(self.simple_color, self.rect)

    def make_highlight(self):
        self.is_high=True

    def make_simple(self):
        self.is_high=False





