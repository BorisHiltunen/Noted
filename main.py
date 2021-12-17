#Importing necessary modules or methods
import pygame
#Will be used soon
#from random import randint

class Noted:
    #Initializing necessary attributes
    def __init__(self):

        pygame.init()

        self.download_pictures()

        self.right_note = pygame.mixer.Sound('right_note.wav')
        self.wrong_timing = pygame.mixer.Sound('wrong_timing.wav')
        self.music = pygame.mixer.music.load('music.wav')

        pygame.mixer.music.play(loops=-1)

        self.height = 700
        self.width = 640

        self.right = False
        self.left = False
        self.down = False
        self.up = False
        self.locked = False

        self.score = 0

        self.falling_notes = []

        #edit this when many can be initialized
        #self.note_amount = 10

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
 
        self.display = pygame.display.set_mode((self.width, self.height))
 
        pygame.display.set_caption("Noted")
 
        self.loop()

    #Function that downloads pictures
    def download_pictures(self):

        self.background = pygame.image.load("background.png")
        self.button1 = pygame.image.load("button1.png")
        self.button1_hover_over = pygame.image.load("button1_hover_over.png")
        self.line = pygame.image.load("line.png")
        self.line_hover_over = pygame.image.load("line_hover_over.png")
        self.note = pygame.image.load("note.png")

    # Function that is responsible that the line works as intended
    def line_engine(self):

        self.line_x = 275 >= self.x-self.line.get_width() and 275 <= self.x+self.line.get_width()
        self.line_y = 575 >= self.y-self.line.get_height() and 575 <= self.y+self.line.get_height()

        if self.note1_hit_y == True or self.note2_hit_y == True or self.note3_hit_y == True or self.note4_hit_y == True:
            self.display.blit(self.line_hover_over, (0, 500))
        else:
            self.display.blit(self.line, (0, 500))

    def note_engine(self):

        self.used_note1 = self.display.blit(self.note, (self.note1_x, self.note1_y))
        self.used_note2 = self.display.blit(self.note, (self.note2_x, self.note2_y))
        self.used_note3 = self.display.blit(self.note, (self.note3_x, self.note3_y))
        self.used_note4 = self.display.blit(self.note, (self.note4_x, self.note4_y))

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

        if self.note1_hit_y == True:
            if self.locked == False:
                if self.right == True:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True
                elif self.left == True:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True
                elif self.up == True:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True
                elif self.down == True:
                    self.right_note.play()
                    self.score += 1
                    self.note1_y = -600
                    self.locked = True

        if self.note2_hit_y == True:
            if self.locked == False:
                if self.right == True:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True
                elif self.left == True:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True
                elif self.up == True:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True
                elif self.down == True:
                    self.right_note.play()
                    self.score += 1
                    self.note2_y = -600
                    self.locked = True

        if self.note3_hit_y == True:
            if self.locked == False:
                if self.right == True:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True
                elif self.left == True:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True
                elif self.up == True:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True
                elif self.down == True:
                    self.right_note.play()
                    self.score += 1
                    self.note3_y = -600
                    self.locked = True

        if self.note4_hit_y == True:
            if self.locked == False:
                if self.right == True:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
                elif self.left == True:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
                elif self.up == True:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
                elif self.down == True:
                    self.right_note.play()
                    self.score += 1
                    self.note4_y = -600
                    self.locked = True
        else:
            if self.locked == False:
                if self.right == True:
                    self.wrong_timing.play()
                    self.score -= 1
                    self.locked = True
                elif self.left == True:
                    self.wrong_timing.play()
                    self.score -= 1
                    self.locked = True
                elif self.up == True:
                    self.wrong_timing.play()
                    self.score -= 1
                    self.locked = True
                elif self.down == True:
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

    # At the moment only watches y
    # therefore needs to be edited if interested in making multiple lanes for the notes

    # Function that is responsible that the notes work as intended
    """def note_engine(self):

        note_y = False

        #self.used_note = self.display.blit(self.note, (self.note1_x, self.note1_y))

        for i in range(self.note_amount):
            self.falling_notes.append([-1000,self.height])
            
        for i in range(self.note_amount):
            #THIS NEEDS TO BE EDITED
            #note_x = 500 >= self.falling_notes[i][0]-self.line.get_height()/2 and 500 <= self.falling_notes[i][0]+self.line.get_height()
            #note_x = self.falling_notes[i][1] >= self.x-self.line.get_height()/2 and self.falling_notes[i][1] <= self.x+self.line.get_height()
            note_y = self.falling_notes[i][1] <= 550 and self.falling_notes[i][1] >= 450

            #print(self.falling_notes[i][1])

            if self.falling_notes[i][1]+self.note.get_height() < self.height+200:
                self.falling_notes[i][1] += 2
            if note_y:
                #print(f"here{self.falling_notes[i][1]}")
                if self.locked == False:
                    if self.right == True:
                        self.score += 1
                        self.falling_notes[i][0] = 300
                        self.falling_notes[i][1] = -randint(100,1000)
                        self.locked = True
                    elif self.left == True:
                        self.score += 1
                        self.falling_notes[i][0] = 300
                        self.falling_notes[i][1] = -randint(100,1000)
                        self.locked = True
                    elif self.up == True:
                        self.score += 1
                        self.falling_notes[i][0] = 300
                        self.falling_notes[i][1] = -randint(100,1000)
                        self.locked = True
                    elif self.down == True:
                        self.score += 1
                        self.falling_notes[i][0] = 300
                        self.falling_notes[i][1] = -randint(100,1000)
                        self.locked = True
            else:

                if self.falling_notes[i][0] < -self.line.get_width() or self.falling_notes[i][0] > self.width:
                    self.falling_notes[i][0] = 275
                    self.falling_notes[i][1] = -randint(100,600)

                    #locked to use so it is impossible to lose points while holding button down
                    # also needs to check why you lose 100 points at a time
                    if self.locked == False:
                        if self.right == True:
                            self.score -= 1
                            self.locked = True
                        elif self.left == True:
                            self.score -= 1
                            self.locked = True
                        elif self.up == True:
                            self.score -= 1
                            self.locked = True
                        elif self.down == True:
                            self.score -= 1
                            self.locked = True
                else:
                    if self.falling_notes[i][1]+self.note.get_height()/2 >= self.height+100:
                        self.falling_notes[i][0] = 275
                        self.falling_notes[i][1] = -randint(100,600)

                    if self.locked == False:
                        if self.right == True:
                            self.score -= 1
                            self.locked = True
                        elif self.left == True:
                            self.score -= 1
                            self.locked = True
                        elif self.up == True:
                            self.score -= 1
                            self.locked = True
                        elif self.down == True:
                            self.score -= 1
                            self.locked = True"""

    # Function that is responsible that the button's work as intended
    def button_engine(self):

        self.line_x = 0 >= self.note1_x-self.line.get_width() and 0 <= self.note1_x+self.line.get_width()
        self.line_y = 500 >= self.note1_y-self.line.get_height() and 500 <= self.note1_y+self.line.get_height()

        if self.line_x and self.line_y:
            if self.right == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            elif self.left == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            elif self.up == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            elif self.down == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            else:
                self.used_button = self.display.blit(self.button1, (275, 575)) 
        else:
            if self.right == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            elif self.left == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            elif self.up == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            elif self.down == True:
                self.used_button = self.display.blit(self.button1_hover_over, (275, 575))
            else:
                self.used_button = self.display.blit(self.button1, (275, 575)) 

    # Function that loops over and over
    # Thus making the game flow
    def loop(self):
        clock = pygame.time.Clock()

        while True:
            self.analyse_events()

            self.draw_the_game()

            clock.tick(60)

    # Function that is mostly responsible that the button's internal operating works as intended
    def analyse_events(self):

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

    #Function that basically draws the game
    def draw_the_game(self):
 
        self.display.fill((0,100,100))

        self.display.blit(self.background, (0, 0))

        self.line_engine()

        self.note_engine()

        #edit this when many can be initialized
        #for i in range(self.note_amount):
            #self.display.blit(self.note, (self.falling_notes[i][0], self.falling_notes[i][1]))

        fontt = pygame.font.SysFont("Arial", 24)
        pygame.draw.rect(self.display, (0, 0, 0), (10, 10, 150, 28))
        text = fontt.render(f"Score: {self.score}", True, (255, 255, 255))
        self.display.blit(text, (10, 10))
            
        self.button_engine()
        
        pygame.display.flip()

#Used to execute code if the file is run directly
if __name__ == "__main__":
    Noted()