import pygame
from pygame.locals import *
from sys import exit
from personagem import Personagem #importa a classe do outro arquivo
from sapato import Sapato
from microfone2 import Microfone
from relogio import Relogio
from constantes import *
from telas import Tela_inicial, Tela_game_over, Tela_vitoria
from zumbi import Zumbi

def restart():
    global inicio, game_over, venceu, time_left_seconds, n_microfones, n_relogios, n_sapatos, zumbi_hits
    #inicio = True
    game_over = venceu = False
    time_left_seconds = initial_time_seconds
    n_sapatos = n_microfones = n_relogios = zumbi_hits = 0
    michael.rect.topleft = michael.x_inicial, michael.y_inicial

pygame.init()
pygame.mixer.init()

#definindo as variaveis dos pontos 
n_sapatos = n_microfones = n_relogios = 0
zumbi_hits = 0 #encontros com zumbi -- contador

#fontes
fonte = pygame.font.SysFont('Calibri', 35, True, False) #negrito e italico 
fonte2 = pygame.font.SysFont('Calibri', 25, False, True) #negrito e italico 
mensagem_danca = 'Pressione Espaço para fazer o Michael dançar!'
danca_formatada = fonte2.render(mensagem_danca, True, verde)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('ESCAPE THRILLER')
clock = pygame.time.Clock()

fundo = pygame.image.load(os.path.join(diretorio_imagens, 'fundo_cemiterio.jpeg')).convert_alpha() #carrega a imagem
fundo = pygame.transform.scale(fundo,(largura, altura)) #muda as dimenções

todas_sprites = pygame.sprite.Group() #classe com todas as sprites
michael = Personagem()
sapato = Sapato()
microfone = Microfone()
relogio = Relogio()

#ZUMBIS
zumbi1 = Zumbi()
zumbi1.rect.x = 0
zumbi1.rect.y = 60

zumbi2 = Zumbi()
zumbi2.rect.x = 700
zumbi2.rect.y = 200

zumbi3 = Zumbi()
zumbi3.rect.x = 350
zumbi3.rect.y = 400

# adicionar aos grupos
todas_sprites.add(michael, sapato, microfone, relogio, zumbi1, zumbi2, zumbi3)

grupo_zumbi = pygame.sprite.Group()
grupo_zumbi.add(zumbi1, zumbi2, zumbi3)

grupo_sapato = pygame.sprite.Group()
grupo_sapato.add(sapato)
grupo_microfone = pygame.sprite.Group()
grupo_microfone.add(microfone)
grupo_relogio = pygame.sprite.Group()
grupo_relogio.add(relogio)

#cronômetro
# O tempo inicial em segundos (60 segundos = 1 minuto de jogo)
initial_time_seconds = 45
time_left_seconds = initial_time_seconds

# Cria um evento de usuário personalizado que será acionado a cada segundo (1000ms)
COUNTDOWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COUNTDOWN_EVENT, 1000) # Dispara o evento a cada 1000 milissegundos

# variáveis do estado do jogo
game_over = False
venceu = False
inicio = True

#variaveis para testar o zumbi
colidindo_zumbi = False

#musica de fundo efeitos sonoros
pygame.mixer.music.set_volume(0.09)
musica_de_fundo = pygame.mixer.music.load(os.path.join(diretorio_sons, 'thriller.mp3')) #música de fundo
pygame.mixer.music.play(-1)      #toca (-1 para ficar repetindo)

barulho_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'colisao_zumbi.wav'))
barulho_colisao.set_volume(1)

barulho_coletaveis = pygame.mixer.Sound(os.path.join(diretorio_sons, 'som_coletaveis.wav'))
barulho_coletaveis.set_volume(0.8)

barulho_vitoria = pygame.mixer.Sound(os.path.join(diretorio_sons, 'he_hee.mp3'))
barulho_vitoria.set_volume(0.6)


#LOOP PRINCIPAL

while True: 
    clock.tick(30) #fps da tela

    if inicio:
        Tela_inicial(tela)
        inicio = False

    if game_over:
        Tela_game_over(tela)
        restart()

    #exibição dos pontos 
    mensagem_sapato = f'Sapatos: {n_sapatos}/{meta}'
    mensagem_microfone = f'Microfones: {n_microfones}/{meta}'
    mensagem_relogio = f'Relógios: {n_relogios}/{meta}'
    mensagem_zumbi = f'Colisões: {zumbi_hits}/3'

    #texto formatado -- colocando cor, textura e a mensagem juntos. 
    sapato_formatado = fonte.render(mensagem_sapato, True, branco)
    microfone_formatado = fonte.render(mensagem_microfone, True, branco)
    relogio_formatado = fonte.render(mensagem_relogio, True, branco)
    zumbi_formatado = fonte.render(mensagem_zumbi, True, vermelho)
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit() # função de sys para fechar

        if event.type == KEYDOWN: #se apertar uma tecla

            if event.key == K_SPACE: #no espaço ele dança
                michael.dancar()

            if event.key == K_RETURN and inicio == True: #restart do jogo
                restart()

        if not game_over and not venceu:
            # Verifica se o evento do cronômetro personalizado foi disparado
            if event.type == COUNTDOWN_EVENT:
                time_left_seconds -= 1
                if time_left_seconds <= 0:
                    game_over = True
                    time_left_seconds = 0 # Garante que o contador não mostre números negativos

    
    if zumbi_hits >= 3:
        game_over = True
        venceu = inicio = False

    #condição de vitoria
    if (n_sapatos >= meta) and (n_microfones >= meta) and (n_relogios >= meta):
        barulho_vitoria.play()
        Tela_vitoria(tela)
        restart() #quando o looping da tela_vitoria acabar, significa que deu restart

    else:
        tela.blit(fundo, (0,0)) #adiciona a imagem de fundo na origem na tela

        #movimento com wasd e setinhas
        if (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]) and (michael.rect.x - 7 > 0): #a segunda condição é pra michael não sair da tela
            michael.rect.x -= 7

        if (pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]) and (michael.rect.x + 7 < largura - 50):
            michael.rect.x += 7

        if (pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]) and (michael.rect.y - 7 > -40):
            michael.rect.y -= 7

        if (pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]) and (michael.rect.y + 7 < altura - 150):
            michael.rect.y += 7

        #COLISÕES
        colisao_sapato = pygame.sprite.spritecollide(michael, grupo_sapato, False, pygame.sprite.collide_mask)
        colisao_micro = pygame.sprite.spritecollide(michael, grupo_microfone, False, pygame.sprite.collide_mask)
        colisao_relogio = pygame.sprite.spritecollide(michael, grupo_relogio, False, pygame.sprite.collide_mask)
        colisao_zumbi = pygame.sprite.spritecollide(michael, grupo_zumbi, False, pygame.sprite.collide_mask)

        if colisao_sapato:
            sapato.muda_posicao()
            n_sapatos += 1
            barulho_coletaveis.play()

        if colisao_micro:
            microfone.muda_posicao()
            n_microfones += 1
            barulho_coletaveis.play()

        if colisao_relogio:
            relogio.muda_posicao()
            n_relogios += 1
            barulho_coletaveis.play()

        if colisao_zumbi:
            if not colidindo_zumbi:
                zumbi_hits += 1
                colidindo_zumbi = True
                barulho_colisao.play()

                if zumbi_hits >= 3:
                    game_over = True
        else:
            colidindo_zumbi = False

        todas_sprites.draw(tela) #sprite aparece na tela
        todas_sprites.update() # atualiza a imagem

        #tela.blit faz o texto formatdo aparecer na tela. 
        tela.blit(sapato_formatado, (20, 20))
        tela.blit(microfone_formatado, (240, 20))
        tela.blit(relogio_formatado, (500, 20))
        tela.blit(zumbi_formatado, (20, 580))
        tela.blit(danca_formatada, (520, 580))


        if not game_over:
            # Formata o tempo para MM:SS
            minutos = time_left_seconds // 60
            segundos = time_left_seconds % 60
            timer_text = f"{minutos:02}:{segundos:02}"
            
            # exibe o cronômetro na tela
            text_surface = fonte.render(timer_text, True, branco)
            tela.blit(text_surface, (930,20))

        else: #ele perdeu pelo fim do tempo
            Tela_game_over(tela)
            restart()


    pygame.display.flip() #atualiza o jogo a cada interação

