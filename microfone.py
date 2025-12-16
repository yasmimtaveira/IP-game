from constantes import *
import pygame
from random import randrange
import os

class Microfone(pygame.sprite.Sprite):
    def __init__(self):
        #inicializa  a classe Sprite com init
        pygame.sprite.Sprite.__init__(self)

        #carrega a imagem do microfone
        self.image = pygame.image.load(os.path.join(diretorio_imagens, 'microfone.png')).convert_alpha()

        #redimensionar a sprite
        # self.image = pygame.transform.scale(self.image, (40, 40))

        #cria o rect
        self.rect = self.image.get_rect()

        # posição inicial aleatória na tela
        self.rect.y = randrange(40, altura - 100, 40)
        self.rect.x = randrange(40, largura - 100, 40)

        #máscara para colisão pixel-perfect (mais precisa que rect)
        self.mask = pygame.mask.from_surface(self.image)
