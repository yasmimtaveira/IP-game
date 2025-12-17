import pygame
from pygame.locals import *
from sys import exit
from constantes import *

pygame.init()

def Tela_inicial(tela):
    # Carregar imagem de fundo inicial
    fundo = pygame.image.load(os.path.join(diretorio_imagens, 'Telainicial.jpg')).convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    inicio = True
    while inicio:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit() # função de sys para fechar

            # Detectar tecla pressionada
            if event.type == KEYDOWN:
                if event.key == K_RETURN:  # ENTER
                    inicio = False               # sai do loop

        # Desenhar o fundo
        tela.blit(fundo, (0, 0))

        pygame.display.update()

    # Carregar imagem de fundo com instruções
    fundo = pygame.image.load(os.path.join(diretorio_imagens, 'menu.png')).convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    menu = True
    while menu:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit() # função de sys para fechar

            # Detectar tecla pressionada
            if event.type == KEYDOWN:
                if event.key == K_RETURN:  # ENTER
                    menu = False   

        # Desenhar o fundo
        tela.blit(fundo, (0, 0))

        pygame.display.update()


def Tela_game_over(tela):
    # Carregar imagem de fundo inicial
    fundo = pygame.image.load(os.path.join(diretorio_imagens, 'game_over.png')).convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    fonte = pygame.font.SysFont('Calibri', 30, True, True) #negrito e italico 

    texto = 'Aperte ENTER para jogar novamente!'
    texto_formatado = fonte.render(texto, True, verde)

    flag = True
    while flag:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit() # função de sys para fechar

            # Detectar tecla pressionada
            if event.type == KEYDOWN:
                if event.key == K_RETURN:  # ENTER
                    flag = False               # sai do loop

        # Desenhar o fundo e o texto
        tela.blit(fundo, (0, 0))
        tela.blit(texto_formatado, (290, 550))

        pygame.display.update()

def Tela_vitoria(tela):
    # Carregar imagem de fundo inicial
    fundo = pygame.image.load(os.path.join(diretorio_imagens, 'vitoria.png')).convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    flag = True
    while flag:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit() # função de sys para fechar

            # Detectar tecla pressionada
            if event.type == KEYDOWN:
                if event.key == K_RETURN:  # ENTER
                    flag = False               # sai do loop

        # Desenhar o fundo
        tela.blit(fundo, (0, 0))

        pygame.display.update()