import pygame
from constantes import *

pygame.init()

def Tela_inicial(tela, inicio):
    # Carregar imagem de fundo inicial
    fundo = pygame.image.load(os.path.join(diretorio_imagens, 'Telainicial.jpg')).convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    while inicio:
        for event in pygame.event.get():

            # Detectar tecla pressionada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # ENTER
                    inicio = False               # sai do loop

        # Desenhar o fundo
        tela.blit(fundo, (0, 0))

        pygame.display.update()
