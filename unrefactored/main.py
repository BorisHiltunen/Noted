"""main.py: Contains Noted class"""

import pygame


class Noted:
    """
    Class that contains every necessary function
    for making Noted app work as intended.
    """

    def __init__(self):

        pygame.init()

        self.download_pictures()

        self.height = 700
        self.width = 640

        self.right = False
        self.left = False
        self.down = False
        self.up = False
        self.locked = False

        self.score = 0

        self.falling_notes = []

        self.x = 0
        self.y = 500

        self.note1_x = 275
        self.note1_y = 0
        self.note1_hit_y = False
        self.note2_x = 275
        self.note2_y = -200
        self.note2_hit_y = False
        self.note3_x = 275
        self.note3_y = -400
        self.note3_hit_y = False
        self.note4_x = 275
        self.note4_y = -600
        self.note4_hit_y = False

        self.line_x = False
        self.line_y = False

        self.used_note1 = ""
        self.used_note2 = ""
        self.used_note3 = ""
        self.used_note4 = ""

        self.used_button = ""

        self.display = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Noted")

        self.sound_manager()
        self.loop()

    def download_pictures(self):
        """Function that downloads pictures."""

        self.background = pygame.image.load("background.png")
        self.button1 = pygame.image.load("button1.png")
        self.button1_hover_over = pygame.image.load("button1_hover_over.png")
        self.line = pygame.image.load("line.png")
        self.line_hover_over = pygame.image.load("line_hover_over.png")
        self.note = pygame.image.load("note.png")

    def sound_manager(self):
        """Function that initializes game's sounds and music."""

        self.right_note = pygame.mixer.Sound("right_note.wav")
        self.wrong_timing = pygame.mixer.Sound("wrong_timing.wav")
        self.music = pygame.mixer.music.load("music.wav")
        pygame.mixer.music.play(loops=-1)

    def line_engine(self):
        """Function that is responsible that the line works as intended."""

        first_condition_for_line_x = 275 >= self.x-self.line.get_width()
        second_condition_for_line_x = 275 <= self.x+self.line.get_width()
        self.line_x = first_condition_for_line_x and \
            second_condition_for_line_x

        first_condition_for_line_y = 575 >= self.y-self.line.get_height()
        second_condition_for_line_y = 575 <= self.y+self.line.get_height()
        self.line_y = first_condition_for_line_y and \
            second_condition_for_line_y

        if self.note1_hit_y or self.note2_hit_y or self.note3_hit_y or \
                self.note4_hit_y:
            self.display.blit(self.line_hover_over, (0, 500))
        else:
            self.display.blit(self.line, (0, 500))

    def note_engine(self):
        """Function that is responsible that the notes work as intended."""

        self.used_note1 = self.display.blit(
            self.note, (self.note1_x, self.note1_y)
            )
        self.used_note2 = self.display.blit(
            self.note, (self.note2_x, self.note2_y)
            )
        self.used_note3 = self.display.blit(
            self.note, (self.note3_x, self.note3_y)
            )
        self.used_note4 = self.display.blit(
            self.note, (self.note4_x, self.note4_y)
            )

        if self.note1_y >= 400 and self.note1_y <= 550:
            self.note1_hit_y = True
        else:
            self.note1_hit_y = False

        if self.note2_y >= 400 and self.note2_y <= 550:
            self.note2_hit_y = True
        else:
            self.note2_hit_y = False

        if self.note3_y >= 400 and self.note3_y <= 550:
            self.note3_hit_y = True
        else:
            self.note3_hit_y = False

        if self.note4_y >= 400 and self.note4_y <= 550:
            self.note4_hit_y = True
        else:
            self.note4_hit_y = False

        if self.note1_hit_y:
            if self.locked is False:
                if self.right:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True
                elif self.left:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True
                elif self.up:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True
                elif self.down:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True

        if self.note2_hit_y:
            if self.locked is False:
                if self.right:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True
                elif self.left:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True
                elif self.up:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True
                elif self.down:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True

        if self.note3_hit_y:
            if self.locked is False:
                if self.right:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True
                elif self.left:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True
                elif self.up:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True
                elif self.down:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True

        if self.note4_hit_y:
            if self.locked is False:
                if self.right:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
                elif self.left:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
                elif self.up:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
                elif self.down:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
        else:
            if self.locked is False:
                if self.right:
                    self.wrong_timing.play()
                    self.score -= 1
                    self.locked = True
                elif self.left:
                    self.wrong_timing.play()
                    self.score -= 1
                    self.locked = True
                elif self.up:
                    self.wrong_timing.play()
                    self.score -= 1
                    self.locked = True
                elif self.down:
                    self.wrong_timing.play()
                    self.score -= 1
                    self.locked = True

        if self.note1_y > self.height:
            self.note1_y = -100
        if self.note2_y > self.height:
            self.note2_y = -100
        if self.note3_y > self.height:
            self.note3_y = -100
        if self.note4_y > self.height:
            self.note4_y = -100

    def button_engine(self):
        """Function that is responsible that the button's work as intended"""

        first_condition_for_line_x = 0 >= \
            self.note1_x-self.line.get_width()
        second_condition_for_line_x = 0 <= \
            self.note1_x+self.line.get_width()
        self.line_x = first_condition_for_line_x and \
            second_condition_for_line_x

        first_condition_for_line_y = 500 >= \
            self.note1_y-self.line.get_height()
        second_condition_for_line_y = 500 <= \
            self.note1_y+self.line.get_height()
        self.line_y = first_condition_for_line_y and \
            second_condition_for_line_y

        if self.line_x and self.line_y:
            if self.right:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            elif self.left:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            elif self.up:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            elif self.down:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            else:
                self.used_button = self.display.blit(
                    self.button1, (275, 575)
                    )
        else:
            if self.right:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            elif self.left:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            elif self.up:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            elif self.down:
                self.used_button = self.display.blit(
                    self.button1_hover_over, (275, 575)
                    )
            else:
                self.used_button = self.display.blit(
                    self.button1, (275, 575)
                    )

    def loop(self):
        """
        Function that loops over and over.
        Thus making the game flow.
        """

        clock = pygame.time.Clock()

        while True:
            self.analyse_events()

            self.draw_the_game()

            clock.tick(60)

    def analyse_events(self):
        """
        Function that is mostly responsible
        that the button's internal operating works as intended.
        """

        self.note1_y += 2
        self.note2_y += 2
        self.note3_y += 2
        self.note4_y += 2

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                    self.locked = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                    self.locked = False
                if event.key == pygame.K_UP:
                    self.up = False
                    self.locked = False
                if event.key == pygame.K_DOWN:
                    self.down = False
                    self.locked = False
            if event.type == pygame.QUIT:
                exit()

    def draw_the_game(self):
        """Function that basically draws the game."""

        self.display.fill((0, 100, 100))

        self.display.blit(self.background, (0, 0))

        self.line_engine()

        self.note_engine()

        fontt = pygame.font.SysFont("Arial", 24)
        pygame.draw.rect(self.display, (0, 0, 0), (10, 10, 150, 28))
        text = fontt.render(f"Score: {self.score}", True, (255, 255, 255))
        self.display.blit(text, (10, 10))

        self.button_engine()

        pygame.display.flip()


if __name__ == "__main__":
    Noted()
