"""
game_data.py:
Initializes and preserves the needed attributes for future use.
"""

import pygame
from app import file_management

pygame.init()

file_management.download_pictures()
file_management.sound_manager()

height = 700
width = 640

right = False
left = False
down = False
up = False
locked = False

score = 0

falling_notes = []

x = 0
y = 500

note1_x = 275
note1_y = 0
note1_hit_y = False
note2_x = 275
note2_y = -200
note2_hit_y = False
note3_x = 275
note3_y = -400
note3_hit_y = False
note4_x = 275
note4_y = -600
note4_hit_y = False

line_x = False
line_y = False

used_note1 = ""
used_note2 = ""
used_note3 = ""
used_note4 = ""

used_button = ""

display = pygame.display.set_mode((width, height))

pygame.display.set_caption("Noted")
