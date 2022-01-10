"""event_analyser.py: Contains function that analyses the game's events."""

import pygame
from app import game_data


def analyse_events():
    """
    Function that is mostly responsible
    that the button's internal operating works as intended.
    """

    game_data.note1_y += 2
    game_data.note2_y += 2
    game_data.note3_y += 2
    game_data.note4_y += 2

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game_data.left = True
            if event.key == pygame.K_RIGHT:
                game_data.right = True
            if event.key == pygame.K_UP:
                game_data.up = True
            if event.key == pygame.K_DOWN:
                game_data.down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                game_data.left = False
                game_data.locked = False
            if event.key == pygame.K_RIGHT:
                game_data.right = False
                game_data.locked = False
            if event.key == pygame.K_UP:
                game_data.up = False
                game_data.locked = False
            if event.key == pygame.K_DOWN:
                game_data.down = False
                game_data.locked = False
        if event.type == pygame.QUIT:
            exit()
