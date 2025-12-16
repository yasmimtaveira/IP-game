from constantes import *
import pygame
from random import randrange


class Sapato(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(os.path.join(diretorio_imagens, 'relogio.png'))
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(40, 440, 50)
        self.rect.x = randrange(50, 750, 50)
        self.mask = pygame.mask.from_surface(self.image)