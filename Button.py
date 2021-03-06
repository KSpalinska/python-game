import pygame
from Constants import *

class Button():

    def __init__(self,title,color_r,color_g,color_b,width,height):
        self.title = title
        self.color_r = color_r
        self.color_g = color_g
        self.color_b =  color_b
        self.width = width
        self.height = height


    def create_surface(self):

        border = 2

        if self.title == BUTTON_PLAY or self.title == BUTTON_INFO:
            myfont = pygame.font.SysFont("notosanscjkkr", int(self.height/2))

        if self.title == BUTTON_CHECK or self.title == BUTTON_RETRY:
            myfont = pygame.font.SysFont("notosanscjkkr", int(self.width/12))

        surface = pygame.Surface([self.width+2*border,self.height+2*border], pygame.SRCALPHA, 32)

        pygame.draw.rect(surface,(0,0,0),pygame.Rect(0,0,self.width+border,self.height+border))
        pygame.draw.rect(surface,(self.color_r, self.color_g, self.color_b),pygame.Rect(border,border,self.width-border,self.height-border))

        label = myfont.render(self.title, 1, (255, 255, 0))
        surface.blit(label,[(self.width+2*border)/10,(self.height+2*border)/10])

        return surface

