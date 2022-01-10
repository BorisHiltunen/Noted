"""
roller.py: file that contains two functions.
One for sending a message if the player won
and the other one for looping over and over
thus making the game flow.
"""

import pygame
from app import game_visualizer
from app import event_analyzer


def loop():
    """
    Function that loops over and over.
    Thus making the game flow.
    """

    clock = pygame.time.Clock()

    while True:
        event_analyzer.analyse_events()

        game_visualizer.draw_the_game()

        clock.tick(60)
