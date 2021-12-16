#Importing necessary modules or methods
import pygame

class Noted:
    #Initializing necessary attributes
    def __init__(self):

        pygame.init()

        self.download_pictures()

        self.height = 700
        self.width = 640

        self.right = False
        self.left = False
        self.down = False
        self.up = False

        self.score = ""

        self.x = 300
        self.y = 300

        self.note_y = -1000
 
        self.display = pygame.display.set_mode((self.width, self.height))
 
        pygame.display.set_caption("Noted")
 
        self.loop()

    #Function that downloads pictures
    def download_pictures(self):

        self.background = pygame.image.load("background.png")
        self.button1 = pygame.image.load("button1.png")
        self.button1_hover_over = pygame.image.load("button1_hover_over.png")
        self.line = pygame.image.load("line.png")
        self.note = pygame.image.load("note.png")

    def notes(self):

        self.used_note = self.display.blit(self.note, (300, self.note_y))

    def buttons(self):

        self.line_x = 0 >= self.x-self.line.get_width() and 0 <= self.x+self.line.get_width()
        self.line_y = 500 >= self.y-self.button1.get_height() and 500 <= self.y+self.button1.get_height()

        if self.line_x and self.line_y:
            if self.right == True:
                self.used_button = self.display.blit(self.button1_hover_over, (100, 500))
            if self.left == True:
                self.used_button = self.display.blit(self.button1_hover_over, (100, 500))
            if self.up == True:
                self.used_button = self.display.blit(self.button1_hover_over, (100, 500))
            if self.down == True:
                self.used_button = self.display.blit(self.button1_hover_over, (100, 500))
            else:
                self.used_button = self.display.blit(self.button1, (100, 500)) 

    #Function that loops over and over
    #Thus making the game flow
    def loop(self):
        clock = pygame.time.Clock()

        while True:
            self.analyse_events()

            self.draw_the_game()

            clock.tick(60)

    #Function that is mostly responsible for the way the character is moving
    def analyse_events(self):

        self.note_y += 10

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

        self.display.blit(self.line, (0, 500))

        self.notes()
            
        self.buttons()
        
        pygame.display.flip()

#Used to execute code if the file is run directly
if __name__ == "__main__":
    Noted()