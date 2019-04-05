import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    """
    Inicialzaa o jogo
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Destrua os Meteoros!")

    # Cria o botão Jogar
    play_button = Button(ai_settings, screen, "Jogar")

    # Cria uma estância que armazena dados estatísticos do jogo
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)

    # Cria um grupo no qual serão armazenados os projéteis e metoros
    bullets = Group()

    meteors = Group()

    # Cria um meteoro
    gf.create_fleet(ai_settings, screen, ship, meteors)

    # Inicializa o laço principal do jogo
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, meteors, bullets)

        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, meteors, bullets)
            gf.update_meteors(ai_settings, stats, screen, ship, meteors, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, meteors, bullets, play_button)


run_game()
