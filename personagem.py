import pygame
from constantes import *

pygame.init()

class Personagem(pygame.sprite.Sprite): #classe personagem herda da classe sprite de Pygame
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #inicializa a classe herdada

        #Atributos
        self.sprites = [] #lista que fica as imagens do michael
        self.sprites.append(pygame.image.load(os.path.join(diretorio_imagens, 'michael.png')).convert_alpha())
        self.sprites.append(pygame.image.load(os.path.join(diretorio_imagens, 'm2.png')).convert_alpha())
        self.sprites.append(pygame.image.load(os.path.join(diretorio_imagens, 'm3.png')).convert_alpha())
        self.sprites.append(pygame.image.load(os.path.join(diretorio_imagens, 'm4.png')).convert_alpha())

        self.x_inicial = 20
        self.y_inicial = 50

        self.x = self.x_inicial #coordenadas iniciais de michael
        self.y = self.y_inicial

        self.atual = 0
        self.image = self.sprites[self.atual] #inicia a animação na primeira imagem
        self.image = pygame.transform.scale(self.image, (200/3,512/3)) #muda o tamanho da imagem (pixels)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y #posição do canto superior esquerdo da imagem
        self.mask = pygame.mask.from_surface(self.image)

        self.animar = False

    #metódos do personagem (animação apenas)
    def update(self):
        if self.animar == True: #atualiza o indice da lista sprite pra passar para prox imagem
            self.atual += 0.2

            if self.atual >= len(self.sprites): #quando chega na ultima imagem, para a animação e reinicia self.atual
                self.atual = 0
                self.animar = False
                
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (200/3,512/3))

    def dancar(self):
        self.animar = True