

class Settings():
    """
    Classe que armazena as configurações
    """

    def __init__(self):
        """
        Inicializa as configurações do jogo
        """
        # Configurações da tela
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Configuração da espaçonave
        self.ship_speed_factor = 1

        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
