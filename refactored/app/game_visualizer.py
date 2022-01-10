"""
game_visualizer:
File that contains function that basically draws the game.
"""

import pygame
from app import game_data
from app import line_management
from app import button_management
from app import note_management


def draw_the_game():
    """Function that basically draws the game."""

    game_data.display.fill((0, 100, 100))

    game_data.display.blit(game_data.background, (0, 0))

    line_management.line_engine()

    note_management.note_engine()

    fontt = pygame.font.SysFont("Arial", 24)
    pygame.draw.rect(game_data.display, (0, 0, 0), (10, 10, 150, 28))
    text = fontt.render(f"Score: {game_data.score}", True, (255, 255, 255))
    game_data.display.blit(text, (10, 10))

    button_management.button_engine()

    pygame.display.flip()
