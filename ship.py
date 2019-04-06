import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """
        Inicializa a espaçonave e define a posição inicial
        """

        super(Ship, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave
        self.image = pygame.image.load('images/rocketb.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicia cada nova espaçonave parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.top = self.screen_rect.top

        # Armazena um valor decimal para o centro da nave
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """
        Atualiza a posição de acordo com o movimento
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com o self.center
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """
        Desenha a espaçonave em sua posição atual
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza a espaçonave na tela"""
        self.center_x = self.screen_rect.centerx
        self.center_y = (self.screen_rect.bottom - 50)
