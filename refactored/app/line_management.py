"""
line_management.py:
File that contains function
that is responsible that the line works as intended.
"""

from app import game_data


def line_engine():
    """Function that is responsible that the line works as intended."""

    first_condition_for_line_x = 275 >= \
        game_data.x-game_data.line.get_width()
    second_condition_for_line_x = 275 <= \
        game_data.x+game_data.line.get_width()
    game_data.line_x = first_condition_for_line_x and \
        second_condition_for_line_x

    first_condition_for_line_y = 575 >= \
        game_data.y-game_data.line.get_height()
    second_condition_for_line_y = 575 <= \
        game_data.y+game_data.line.get_height()
    game_data.line_y = first_condition_for_line_y and \
        second_condition_for_line_y

    if game_data.note1_hit_y or game_data.note2_hit_y or \
            game_data.note3_hit_y or game_data.note4_hit_y:
        game_data.display.blit(game_data.line_hover_over, (0, 500))
    else:
        game_data.display.blit(game_data.line, (0, 500))
