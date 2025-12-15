import pygame

pygame.init()

class Personagem(pygame.sprite.Sprite): #classe personagem herda da classe sprite de Pygame
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #inicializa a classe herdada

        #Atributos
        self.sprites = [] #lista que fica as imagens do michael
        self.sprites.append(pygame.image.load('IP-game/sprites/michael.png'))
        self.sprites.append(pygame.image.load('IP-game/sprites/m2.png'))
        self.sprites.append(pygame.image.load('IP-game/sprites/m3.png'))
        self.sprites.append(pygame.image.load('IP-game/sprites/m4.png'))

        self.x = 0 #coordenadas iniciais de michael
        self.y = 0

        self.atual = 0
        self.image = self.sprites[self.atual] #inicia a animação na primeira imagem
        self.image = pygame.transform.scale(self.image, (200/3,512/3)) #muda o tamanho da imagem (pixels)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y #posição do canto superior esquerdo da imagem

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