import pygame.font


class Button():
    """ Uma classe para botões"""

    def __init__(self, ai_settings, screen, msg):
        """Inicializa os atributos dos botões"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define as dimensões e as propriedades do botão
        self.width = 100
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Constroi o objeto rect do botão e centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # A mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Transforma msg em imagem renderizada"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """desenha um botão e em seguida uma mensagem"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

