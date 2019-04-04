import pygame
from pygame.sprite import Sprite


class Meteor(Sprite):
    """
    Uma classe que representa um meteoro
    """

    def __init__(self, ai_settings, screen):
        """
        Inicializa o meteoro em sua posição inicial
        """
        super(Meteor, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem do meteoro
        self.image = pygame.image.load('images/meteor.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo meteoro próximo à parte superior esquerda
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do meteoro
        self.x = float(self.rect.x)

    def blitme(self):
        """
        Desenha o meteoro em sua posição atual
        """
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Checa se atingiu as bordas"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move meteors para direita"""
        self.x += (self.ai_settings.meteor_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

