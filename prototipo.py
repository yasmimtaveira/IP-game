#criação da janela onde vai se passar o jogo

#IMPORTS DO PYGAME
import pygame 
from pygame.locals import *
from sys import exit  #serve pra fechar a janela do jogo (exit)
from random import randint # função para os objetos, assim que forem coletados, mudarem de localização


#-------------------------------------------------------------------------

#SCRIPT
pygame.init() #inicia as funções e variáveis de toda biblioteca pygame

#dimensão da tela
largura = 1080
altura = 640
x = largura/ 2
y = altura / 2

#variaveis para a localização dos objetos: 
x_objeto1 = randint(20,1060) #depois alterar os intervalos de numeros 
y_objeto1 = randint(20,660)

x_objeto2 = randint(20,1060) #depois alterar os intervalos de numeros 
y_objeto2 = randint(20,660)

x_objeto3 = randint(20,1060) #depois alterar os intervalos de numeros 
y_objeto3 = randint(20,660)

#definindo as variaveis dos pontos 
pontos_azul =0
pontos_laranja =0
pontos_roxo = 0

#fontes
fonte = pygame.font.SysFont('freesansbold.ttf', 25, True, True) #negrito e italico (true)

#tela
tela = pygame.display.set_mode((largura, altura)) #conferir depois

pygame.display.set_caption('THRILLER') #TITULO DA JANELA

#taxa de frames 
relogio = pygame.time.Clock()

#--------------------------------------------------------------------------=

#LOOP PRINCIPAL (infinito) DO JOGO 

while True:
    relogio.tick(30) #modifica frames do jogo
    tela.fill((0,0,0)) # se mover sem aumentar 
    
    #exibição dos pontos 
    mensagem_azul = f'Bolinhas azuis capturadas: {pontos_azul}'
    mensagem_laranja = f'Bolinhas laranjas capturadas: {pontos_laranja}'
    mensagem_roxo = f'Bolinhas roxas capturadas: {pontos_roxo}'
    
    #texto formatado -- colocando cor, textura e a mensagem juntos. 
    texto_formatado1 = fonte.render(mensagem_azul, True, (255, 255, 255))
    texto_formatado2 = fonte.render(mensagem_laranja, True, (255, 255, 255))
    texto_formatado3 = fonte.render(mensagem_roxo, True, (255, 255, 255))
    
    for event in pygame.event.get(): # a cada interação do loop principal vai checar se algum evento ocorreu.
        if event.type == QUIT: #condição para fechar o jogo 
            pygame.quit()
            exit()
            
        #quando apertar alguma tela, o computador deve reconhecer isso     PROVAVELMENTE apagar dps    
        # if event.type == KEYDOWN:
        #     if event.key == K_a: #esquerda
        #         x = x - 20
        #     if event.key == K_d: #direita 
        #         x = x + 20
        #     if event.key == K_w: #cima
        #         y = y - 20
        #     if event.key == K_s: #baixo
        #         y = y + 20
    
    #controlando o retângulo  ( com wasd e com SETINHASSS ) 
    if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
        x = x - 20
    if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
        x = x + 20
    if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
        y = y - 20
    if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
        y = y + 20
    
    #testes para desenhar objetos na tela (adicionando ret para ficar melhor de chamar a o objeto depois...)
    ret_retangulo = pygame.draw.rect(tela,(255,0,0), (x,y, 40, 50)) #parâmetros: (a tela, (tupla com a cor), (x, y, comprimento do retangulo, altura)
    #bolinha azul
    ret_objeto1 = pygame.draw.circle(tela, (0,0,255), (x_objeto1,y_objeto1), 20)
    #bolinha laranja
    ret_objeto2 = pygame.draw.circle(tela, (210,105,30), (x_objeto2,y_objeto2), 20)
    #bolinha roxa
    ret_objeto3 = pygame.draw.circle(tela, (139,0,139), (x_objeto3,y_objeto3), 20)

    #condições de colisão
    if ret_retangulo.colliderect(ret_objeto1):
        x_objeto1 = randint(40,600) #depois alterar os intervalos de numeros 
        y_objeto1 = randint(50,430)
        pontos_azul += 1

    if ret_retangulo.colliderect(ret_objeto2):
        x_objeto2 = randint(40,600) #depois alterar os intervalos de numeros 
        y_objeto2 = randint(50,430)
        pontos_laranja += 1
            
    if ret_retangulo.colliderect(ret_objeto3):
        x_objeto3 = randint(40,600) #depois alterar os intervalos de numeros 
        y_objeto3 = randint(50,430)
        pontos_roxo += 1

   #fazendo aparecer do outro lado
    if x >= largura:
        x = 0
    elif x < 0:
        x = largura - 1

    if y >= altura:
        y = 0
    elif y < 0:
        y = altura - 1

    #tela.blit faz o texto formatdo aparecer na tela. 
    tela.blit(texto_formatado1, (25,600))
    tela.blit(texto_formatado2, (400,600))
    tela.blit(texto_formatado3, (800,600))
    
    pygame.display.update() #LINHA SUPER IMPORTANTE!!!!!!!!!. (sem ela, o jogo roda uma vez e trava)
