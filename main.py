
import pygame
from pygame.locals import *
from sys import exit
from personagem import Personagem #importa a classe do outro arquivo
from sapato import Sapato
from microfone2 import Microfone
from relogio import Relogio
from constantes import *
from tela_inicial import Tela_inicial
from random import randrange
from zumbi import Zumbi

pygame.init()
pygame.mixer.init()

#definindo as variaveis dos pontos 
n_sapatos = 0
n_microfones = 0
n_relogios = 0
zumbi_hits = 0 #encontros com zumbi -- contador

#fontes
fonte = pygame.font.SysFont('freesansbold.ttf', 30, False, False) #negrito e italico 

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('THRILLER')
clock = pygame.time.Clock()

fundo = pygame.image.load(os.path.join(diretorio_imagens, 'chao_cemiterio.jpg')).convert_alpha() #carrega a imagem
fundo = pygame.transform.scale(fundo,(largura, altura)) #muda as dimenções

todas_sprites = pygame.sprite.Group() #classe com todas as sprites
michael = Personagem()
sapato = Sapato()
microfone = Microfone()
relogio = Relogio()

todas_sprites.add(michael)
todas_sprites.add(sapato)
todas_sprites.add(microfone)
todas_sprites.add(relogio)


grupo_sapato = pygame.sprite.Group()
grupo_sapato.add(sapato)
grupo_microfone = pygame.sprite.Group()
grupo_microfone.add(microfone)
grupo_relogio = pygame.sprite.Group()
grupo_relogio.add(relogio)
grupo_zumbi = pygame.sprite.Group()

#------------------------------------------------
#ZUMBIS
zumbi1 = Zumbi()
zumbi1.rect.x = 100
zumbi1.rect.y = 60

zumbi2 = Zumbi()
zumbi2.rect.x = 500
zumbi2.rect.y = 300

# adicionar aos grupos
todas_sprites.add(michael, sapato, microfone, relogio, zumbi1, zumbi2)

grupo_zumbi = pygame.sprite.Group()
grupo_zumbi.add(zumbi1, zumbi2)


#------------------------------------------------

#cronômetro
# O tempo inicial em segundos (60 segundos = 1 minuto de jogo)
initial_time_seconds = 30
time_left_seconds = initial_time_seconds

# Cria um evento de usuário personalizado que será acionado a cada segundo (1000ms)
COUNTDOWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COUNTDOWN_EVENT, 1000) # Dispara o evento a cada 1000 milissegundos

# Variável do fim do jogo
game_over = False
inicio = True

while True: #loop principal
    clock.tick(30) #fps da tela

    if inicio:
        Tela_inicial(tela, inicio)
        inicio = False

    #exibição dos pontos 
    mensagem_sapato = f'Sapatos: {n_sapatos}'
    mensagem_microfone = f'Microfones: {n_microfones}'
    mensagem_relogio = f'Relógios: {n_relogios}'

    #texto formatado -- colocando cor, textura e a mensagem juntos. 
    sapato_formatado = fonte.render(mensagem_sapato, True, branco)
    microfone_formatado = fonte.render(mensagem_microfone, True, branco)
    relogio_formatado = fonte.render(mensagem_relogio, True, branco)
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit() # função de sys para fechar

        if event.type == KEYDOWN: #se apertar uma tecla, ele dança (começa a animação)

            if event.key == K_SPACE:
                michael.dancar()

            if event.key == K_RETURN and inicio == False:
                inicio = True
                game_over = False
                time_left_seconds = initial_time_seconds

        if not game_over:
            # Verifica se o evento do cronômetro personalizado foi disparado
            if event.type == COUNTDOWN_EVENT:
                time_left_seconds -= 1
                if time_left_seconds <= 0:
                    game_over = True
                    time_left_seconds = 0 # Garante que o contador não mostre números negativos

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

    colisoes = pygame.sprite.spritecollide(michael, grupo_sapato, False, pygame.sprite.collide_mask)
    colisao_micro = pygame.sprite.spritecollide(michael, grupo_microfone, False, pygame.sprite.collide_mask)
    colisao_relogio = pygame.sprite.spritecollide(michael, grupo_relogio, False, pygame.sprite.collide_mask)
    #colisao_zumbi = pygame.sprite.spritecollide(michael, grupo_zumbi, False, pygame.sprite.collide_mask)


    if colisoes:
        sapato.rect.y = randrange(40, 440, 50)
        sapato.rect.x = randrange(50, 750, 50)
        n_sapatos += 1

    if colisao_micro:
        microfone.rect.y = randrange(40, 440, 50)
        microfone.rect.x = randrange(50, 750, 50)
        n_microfones += 1

    if colisao_relogio:
        relogio.rect.y = randrange(40, 440, 50)
        relogio.rect.x = randrange(50, 750, 50)
        n_relogios += 1
        
#COLISÃO ZUMBISS---------------------------------
#ESTAVA COM ERRO NISO AQ 
#-----------------------------------------------
            
    todas_sprites.draw(tela) #sprite aparece na tela
    todas_sprites.update() # atualiza a imagem

    #tela.blit faz o texto formatdo aparecer na tela. 
    tela.blit(sapato_formatado, (10, 10))
    tela.blit(microfone_formatado, (200, 10))
    tela.blit(relogio_formatado, (400, 10))


    if not game_over:
        # Formata o tempo para MM:SS
        minutes = time_left_seconds // 60
        seconds = time_left_seconds % 60
        timer_text = f"{minutes:02}:{seconds:02}"
        
        # Renderiza e exibe o cronômetro
        text_surface = fonte.render(timer_text, True, branco)
        tela.blit(text_surface, (700,10))

    else: #ele perdeu pelo fim do tempo
        game_over_formatado = fonte.render('GAME OVER', True, branco)
        tela.fill(preto)
        tela.blit(game_over_formatado, (largura/2 - 50, altura/2 - 30))

    pygame.display.flip() #atualiza o jogo a cada interação


