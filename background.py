import pygame


class Background(pygame.sprite.Sprite):
    """Uma classe para o fundo do jogo"""

    def __init__(self, location):
        """Inicializa a imagem de fundo"""

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/nebula_red.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
