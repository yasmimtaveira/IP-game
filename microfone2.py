from constantes import *
import pygame, os
from random import randrange

class Microfone(pygame.sprite.Sprite):
    def __init__(self):
        #inicializa  a classe Sprite com init
        pygame.sprite.Sprite.__init__(self)

        #carrega a imagem do microfone
        self.image = pygame.image.load(os.path.join(diretorio_imagens, 'microfone.png')).convert_alpha()

        #redimensionar a sprite
        self.image = pygame.transform.scale(self.image, (80, 80))

        #cria o rect
        self.rect = self.image.get_rect()

        # posição inicial aleatória na tela
        self.rect.y = randrange(40, 440, 50)
        self.rect.x = randrange(50, 750, 50)

        #máscara para colisão pixel-perfect (mais precisa que rect)
        self.mask = pygame.mask.from_surface(self.image)
