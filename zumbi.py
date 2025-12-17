from constantes import *
import pygame
from random import randrange
import os

class Zumbi(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image_right = pygame.image.load(os.path.join(diretorio_imagens, 'zumbi direita.png'))
        self.image_right = pygame.transform.scale(self.image_right, (300, 200))
        
        self.image_left = pygame.image.load(os.path.join(diretorio_imagens, 'zumbi esquerda.png'))
        self.image_left = pygame.transform.scale(self.image_left, (300, 200))
        
        
        self.image  = self.image_right  #começa indo para a direita
        
        self.rect = self.image.get_rect()
        #self.rect.x = 0 #definido no main
        #self.rect.y = 0 
        
        self.velocidade_x = 4 #velocidade na horizontal 
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self):
        self.rect.x += self.velocidade_x

        # limite da direita (centro encosta)
        if self.rect.centerx >= largura:
            self.rect.centerx = largura
            self.velocidade_x = -4
            self.image = self.image_left
            self.mask = pygame.mask.from_surface(self.image)

        # limite da esquerda (centro encosta)
        elif self.rect.centerx <= 0:
            self.rect.centerx = 0
            self.velocidade_x = 4
            self.image = self.image_right
            self.mask = pygame.mask.from_surface(self.image)