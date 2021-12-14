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

        self.x = 313
        self.y = 563
 
        self.display = pygame.display.set_mode((self.width, self.height))
 
        pygame.display.set_caption("Noted")
 
        self.loop()

    #Function that downloads pictures
    def download_pictures(self):

        pass
        #self.background = pygame.image.load("background.png")
        #self.button = pygame.image.load("button.png")

    #Function that loops over and over
    #Thus making the game flow
    def loop(self):
        clock = pygame.time.Clock()

        while True:
            self.draw_the_game()

            self.analyse_events()

            clock.tick(60)

            if self.done:
                self.won_the_game()
                break

    #Function that is mostly responsible for the way the character is moving
    def analyse_events(self):

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

        #self.display.blit(self.background, (0, 0))

        self.display.blit(self.button, (self.x, self.y))
 
        pygame.display.flip()

#Used to execute code if the file is run directly
if __name__ == "__main__":
    Noted()