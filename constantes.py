import os

#quantidade de coletaveis
meta = 5

largura = 800*1.3
altura = 480*1.3

#TUPLAS RGB DE CORES
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
ciano = (0, 255, 255)
magenta = (255, 0, 255)

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'sprites')
diretorio_sons = os.path.join(diretorio_principal, 'sons')