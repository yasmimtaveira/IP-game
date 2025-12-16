from random import randint


class Microfone:
    def __init__(self, imagem, cor_tipo):
        
        # imagem do microfone
        # cor_tipo: string apenas para identificar (azul, laranja, roxo) #mexer dpss

        self.imagem = imagem
        self.tipo = cor_tipo
        self.rect = self.imagem.get_rect()
        self.reposicionar()

    def reposicionar(self):
        self.rect.topleft = (randint(40, 600),randint(50, 430))

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

    def verificar_colisao(self, jogador_rect):
        if self.rect.colliderect(jogador_rect):
            self.reposicionar()
            return True
        return False
