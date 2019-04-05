

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

        self.ship_limit = 3

        # Configuração dos projéteis
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Configuração de meteors
        self.fleet_drop_speed = 10
        # fleet igual a 1 represneta direita. -1 esquerda

        # Taxa que a velocidade do jogo aumenta
        self.speedup_scale = 1.1
        # Taxa com que pontos aumentam
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Iniciliza as configurações que mudam no decorrer do jogo"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.meteor_speed_factor = 1
        self.fleet_direction = 1

        # Pontuação
        self.meteor_points = 50

    def increase_speed(self):
        """Aumenta a velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.meteor_speed_factor *= self.speedup_scale
        self.meteor_points = int(self.meteor_points * self.score_scale)
