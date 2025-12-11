import pygame
from pygame.locals import *
from sys import exit

pygame.init()

class Personagem(pygame.sprite.Sprite): #classe personagem herda da classe sprite de Pygame
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #inicializa a classe herdada

        #Atributos
        self.sprites = [] #lista que fica as imagens do michael
        self.sprites.append(pygame.image.load('IP-game/teste_animacao/michael.png'))
        self.sprites.append(pygame.image.load('IP-game/teste_animacao/m2.png'))
        self.sprites.append(pygame.image.load('IP-game/teste_animacao/m3.png'))
        self.sprites.append(pygame.image.load('IP-game/teste_animacao/m4.png'))

        self.atual = 0
        self.image = self.sprites[self.atual] #inicia a animação na primeira imagem
        self.image = pygame.transform.scale(self.image, (200,512)) #muda o tamanho da imagem (pixels)

        self.rect = self.image.get_rect()
        self.rect.topleft = 300,0 #posição do canto superior esquerdo da imagem

        self.animar = False

    #metódos do personagem (animação apenas)
    def update(self):
        if self.animar == True: #atualiza o indice da lista sprite pra passar para prox imagem
            self.atual += 0.15

            if self.atual >= len(self.sprites): #quando chega na ultima imagem, para a animação e reinicia self.atual
                self.atual = 0
                self.animar = False
                
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (200,512))

    def dancar(self):
        self.animar = True


largura = 800
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('aprendendo pygame e poo')
relogio = pygame.time.Clock()

todas_sprites = pygame.sprite.Group() #classe com todas as sprites
michael = Personagem()
todas_sprites.add(michael)

while True: #loop principal
    relogio.tick(30) #fps da tela
    tela.fill((200,200,200))
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit() # função de sys para fechar

        if event.type == KEYDOWN: #se apertar uma tecla, ele dança (começa a animação)
            michael.dancar()

    
    todas_sprites.draw(tela) #sprite aparece na tela
    todas_sprites.update() # atualiza

    pygame.display.flip() #atualiza o jogo a cada interação