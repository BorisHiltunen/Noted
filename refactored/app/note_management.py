"""
note_management.py:
File that contains a function that is responsible
that the notes work as intended.
"""

from app import game_data


def note_engine():
    """Function that is responsible that the notes work as intended."""

    game_data.used_note1 = game_data.display.blit(
        game_data.note, (game_data.note1_x, game_data.note1_y)
        )
    game_data.used_note2 = game_data.display.blit(
        game_data.note, (game_data.note2_x, game_data.note2_y)
        )
    game_data.used_note3 = game_data.display.blit(
        game_data.note, (game_data.note3_x, game_data.note3_y)
        )
    game_data.used_note4 = game_data.display.blit(
        game_data.note, (game_data.note4_x, game_data.note4_y)
        )

    if game_data.note1_y >= 400 and game_data.note1_y <= 550:
        game_data.note1_hit_y = True
    else:
        game_data.note1_hit_y = False

    if game_data.note2_y >= 400 and game_data.note2_y <= 550:
        game_data.note2_hit_y = True
    else:
        game_data.note2_hit_y = False

    if game_data.note3_y >= 400 and game_data.note3_y <= 550:
        game_data.note3_hit_y = True
    else:
        game_data.note3_hit_y = False

    if game_data.note4_y >= 400 and game_data.note4_y <= 550:
        game_data.note4_hit_y = True
    else:
        game_data.note4_hit_y = False

    if game_data.note1_hit_y:
        if game_data.locked is False:
            if game_data.right:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note1_y = -600
                game_data.locked = True
            elif game_data.left:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note1_y = -600
                game_data.locked = True
            elif game_data.up:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note1_y = -600
                game_data.locked = True
            elif game_data.down:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note1_y = -600
                game_data.locked = True

    if game_data.note2_hit_y:
        if game_data.locked is False:
            if game_data.right:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note2_y = -600
                game_data.locked = True
            elif game_data.left:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note2_y = -600
                game_data.locked = True
            elif game_data.up:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note2_y = -600
                game_data.locked = True
            elif game_data.down:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note2_y = -600
                game_data.locked = True

    if game_data.note3_hit_y:
        if game_data.locked is False:
            if game_data.right:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note3_y = -600
                game_data.locked = True
            elif game_data.left:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note3_y = -600
                game_data.locked = True
            elif game_data.up:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note3_y = -600
                game_data.locked = True
            elif game_data.down:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note3_y = -600
                game_data.locked = True

    if game_data.note4_hit_y:
        if game_data.locked is False:
            if game_data.right:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note4_y = -600
                game_data.locked = True
            elif game_data.left:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note4_y = -600
                game_data.locked = True
            elif game_data.up:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note4_y = -600
                game_data.locked = True
            elif game_data.down:
                game_data.right_note.play()
                game_data.score += 1
                game_data.note4_y = -600
                game_data.locked = True
    else:
        if game_data.locked is False:
            if game_data.right:
                game_data.wrong_timing.play()
                game_data.score -= 1
                game_data.locked = True
            elif game_data.left:
                game_data.wrong_timing.play()
                game_data.score -= 1
                game_data.locked = True
            elif game_data.up:
                game_data.wrong_timing.play()
                game_data.score -= 1
                game_data.locked = True
            elif game_data.down:
                game_data.wrong_timing.play()
                game_data.score -= 1
                game_data.locked = True

    if game_data.note1_y > game_data.height:
        game_data.note1_y = -100
    if game_data.note2_y > game_data.height:
        game_data.note2_y = -100
    if game_data.note3_y > game_data.height:
        game_data.note3_y = -100
    if game_data.note4_y > game_data.height:
        game_data.note4_y = -100
