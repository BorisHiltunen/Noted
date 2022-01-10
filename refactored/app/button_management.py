"""
button_management.py:
File that contains a function that is responsible
that the game's buttons work as intended.
"""

from app import game_data


def button_engine():
    """Function that is responsible that the buttons work as intended"""

    first_condition_for_line_x = 0 >= \
        game_data.note1_x-game_data.line.get_width()
    second_condition_for_line_x = 0 <= \
        game_data.note1_x+game_data.line.get_width()
    game_data.line_x = first_condition_for_line_x and \
        second_condition_for_line_x

    first_condition_for_line_y = 500 >= \
        game_data.note1_y-game_data.line.get_height()
    second_condition_for_line_y = 500 <= \
        game_data.note1_y+game_data.line.get_height()
    game_data.line_y = first_condition_for_line_y and \
        second_condition_for_line_y

    if game_data.line_x and game_data.line_y:
        if game_data.right:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        elif game_data.left:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        elif game_data.up:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        elif game_data.down:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        else:
            game_data.used_button = game_data.display.blit(
                game_data.button1, (275, 575)
                )
    else:
        if game_data.right:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        elif game_data.left:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        elif game_data.up:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        elif game_data.down:
            game_data.used_button = game_data.display.blit(
                game_data.button1_hover_over, (275, 575)
                )
        else:
            game_data.used_button = game_data.display.blit(
                game_data.button1, (275, 575)
                )
