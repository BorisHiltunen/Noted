"""
file_management.py:
File that contains two functions that initialize files.
"""

import os
import pygame
from app import game_data


def download_pictures():
    """Function that downloads pictures."""

    game_data.background = pygame.image.load(
        os.path.join("images", "background.png")
        )
    game_data.button1 = pygame.image.load(
        os.path.join("images", "button1.png")
        )
    game_data.button1_hover_over = pygame.image.load(
        os.path.join("images", "button1_hover_over.png")
        )
    game_data.line = pygame.image.load(
        os.path.join("images", "line.png")
        )
    game_data.line_hover_over = pygame.image.load(
        os.path.join("images", "line_hover_over.png")
        )
    game_data.note = pygame.image.load(
        os.path.join("images", "note.png")
        )


def sound_manager():
    """Function that initializes game's sounds and music."""

    game_data.right_note = pygame.mixer.Sound(
        os.path.join("sounds", "right_note.wav")
        )
    game_data.wrong_timing = pygame.mixer.Sound(
        os.path.join("sounds", "wrong_timing.wav")
        )
    game_data.music = pygame.mixer.music.load(
        os.path.join("music", "music.wav")
        )
    pygame.mixer.music.play(loops=-1)
