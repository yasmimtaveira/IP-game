
import pygame
from pygame.locals import *
from sys import exit
from personagem import Personagem #importa a classe do outro arquivo
from constantes import *

pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('THRILLER')
relogio = pygame.time.Clock()

fundo = pygame.image.load(os.path.join(diretorio_imagens, 'chao_cemiterio.jpg')).convert_alpha() #carrega a imagem
fundo = pygame.transform.scale(fundo,(largura, altura)) #muda as dimenções

todas_sprites = pygame.sprite.Group() #classe com todas as sprites
michael = Personagem()
todas_sprites.add(michael)

while True: #loop principal
    relogio.tick(30) #fps da tela
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit() # função de sys para fechar

        if event.type == KEYDOWN: #se apertar uma tecla, ele dança (começa a animação)

            if event.key == K_SPACE:
                michael.dancar()

    tela.blit(fundo, (0,0)) #adiciona a imagem de fundo na origem na tela

    #movimento com wasd
    if pygame.key.get_pressed()[K_a] and (michael.rect.x - 7 > 0): #a segunda condição é pra michael não sair da tela
        michael.rect.x -= 7

    if pygame.key.get_pressed()[K_d] and (michael.rect.x + 7 < largura - 50):
        michael.rect.x += 7

    if pygame.key.get_pressed()[K_w] and (michael.rect.y - 7 > -40):
        michael.rect.y -= 7

    if pygame.key.get_pressed()[K_s] and (michael.rect.y + 7 < altura - 150):
        michael.rect.y += 7

    todas_sprites.draw(tela) #sprite aparece na tela
    todas_sprites.update() # atualiza a imagem

    pygame.display.flip() #atualiza o jogo a cada interação

