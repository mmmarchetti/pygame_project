import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    """
    Inicialzaa o jogo
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Invasão Alien")

    # Cria uma estância que armazena dados estatísticos do jogo
    stats = GameStats(ai_settings)

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()

    meteors = Group()

    # Cria um meteoro
    gf.create_fleet(ai_settings, screen, ship, meteors)

    # Inicializa o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, meteors, bullets)
        # print(len(bullets))
        gf.update_meteors(ai_settings, stats, screen, ship, meteors, bullets)
        gf.update_screen(ai_settings, screen, ship, meteors, bullets)


run_game()
